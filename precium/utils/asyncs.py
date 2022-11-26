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


async def collect_data(
    url: str, session: ClientSession, topic: str, producer: KafkaProducer
):
    payload = await get_event(url=url, session=session)
    if payload is None:
        return

    await send_event(payload=payload, topic=topic, producer=producer)


async def bulk_collect_data(urls: List[str], topic: str, producer) -> None:
    """
    Usage:
        output = asyncio.run(bulk_collect_data(urls=urls))
    """
    sema = asyncio.BoundedSemaphore(5)

    async with ClientSession() as session:
        tasks = list(
            collect_data(url=url, session=session, topic=topic, producer=producer)
            for url in urls
        )
        async with sema:
            await asyncio.gather(*tasks)
