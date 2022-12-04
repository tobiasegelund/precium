"""
Async material used https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
"""
import json
import asyncio
import uuid
import datetime
from typing import List, Optional, Dict, Any
from aiohttp import ClientSession

from kafka.producer import KafkaProducer

from precium.entities.enums import Company


def collect_uid(data: Dict[str, Any], company: Company):
    mapping = {Company.nemlig: "Id"}

    kw = mapping.get(company, None)
    if kw is None:
        raise ValueError(
            f"{company} does not have any realted key-word mapping to find uid.."
        )
    uid = data.get(kw)
    if uid is None:
        raise ValueError(f"{kw} doesn't exists in payload. Something has changed..")

    return uid


async def get_event(url: str, session: ClientSession) -> Optional[str]:
    # logger.info(f"[Info] Fetch {str(url)}")
    response = await session.request(method="GET", url=url)
    if response.status != 200:
        return

    payload = await response.text()
    return payload


async def send_event(
    payload: str, topic: str, company: Company, producer: KafkaProducer, debug: bool
) -> None:
    data = json.loads(payload)
    uid = collect_uid(data, company=company)
    data = {
        "event_id": str(uuid.uuid4()),
        "event_datetime": datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        "uid": uid,
        "company": company.value,
        "payload": data,
    }
    if not debug:
        producer.send(topic, data)

    print(data)


async def bound_collect(
    sem: asyncio.Semaphore,
    url: str,
    session: ClientSession,
    topic: str,
    company: Company,
    producer: KafkaProducer,
    debug: bool,
):
    async with sem:
        payload = await get_event(url=url, session=session)
        if payload is None:
            return

        await send_event(
            payload=payload,
            topic=topic,
            company=company,
            producer=producer,
            debug=debug,
        )


async def bulk_collect(
    urls: List[str],
    topic: str,
    company: Company,
    producer: KafkaProducer,
    debug: bool = True,
) -> None:
    """
    Usage:
        output = asyncio.run(bulk_collect(urls=urls))
    """
    sem = asyncio.Semaphore(5)

    async with ClientSession() as session:
        tasks = list(
            asyncio.ensure_future(
                bound_collect(
                    sem=sem,
                    url=url,
                    session=session,
                    topic=topic,
                    company=company,
                    producer=producer,
                    debug=debug,
                )
            )
            for url in urls
        )
        await asyncio.gather(*tasks)
