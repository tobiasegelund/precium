"""
Async material used https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
"""
import json
import asyncio
import uuid
import datetime
from typing import List, Optional
from aiohttp import ClientSession

from kafka.producer import KafkaProducer


async def get_event(url: str, session: ClientSession) -> Optional[str]:
    # logger.info(f"[Info] Fetch {str(url)}")
    response = await session.request(method="GET", url=url)
    if response.status != 200:
        return

    payload = await response.text()
    return payload


async def send_event(payload: str, topic: str, producer: KafkaProducer) -> None:
    data = {
        "event_id": str(uuid.uuid4()),
        "event_datetime": datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        "payload": json.loads(payload),
    }

    producer.send(topic, data)


async def bound_collect(
    sem: asyncio.Semaphore,
    url: str,
    session: ClientSession,
    topic: str,
    producer: KafkaProducer,
):
    async with sem:
        payload = await get_event(url=url, session=session)
        if payload is None:
            return

        await send_event(payload=payload, topic=topic, producer=producer)


async def bulk_collect_data(urls: List[str], topic: str, producer) -> None:
    """
    Usage:
        output = asyncio.run(bulk_collect_data(urls=urls))
    """
    sem = asyncio.Semaphore(5)

    async with ClientSession() as session:
        tasks = list(
            asyncio.ensure_future(
                bound_collect(
                    sem=sem, url=url, session=session, topic=topic, producer=producer
                )
            )
            for url in urls
        )
        await asyncio.gather(*tasks)
