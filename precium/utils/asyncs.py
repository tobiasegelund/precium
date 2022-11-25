import json
import asyncio
from typing import List, Dict, Any, Optional, Union
from aiohttp import ClientSession


async def get_data(url: str, session: ClientSession) -> Optional[Dict[str, Any]]:
    # logger.info(f"[Info] Fetch {str(url)}")
    response = await session.request(method="GET", url=url)
    if response.status != 200:
        return None
    text = await response.text()

    return json.loads(text)


async def send_data(data: Optional[Dict[str, Any]]):
    pass


async def get_and_send_data_async(urls: List[str]) -> None:
    """
    Usage:
        output = asyncio.run(get_api_data(urls=urls))
    """

    async with ClientSession() as session:
        tasks = list(get_data(url=url, session=session) for url in urls)
        await asyncio.gather(*tasks)
