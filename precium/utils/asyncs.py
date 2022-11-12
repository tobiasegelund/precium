import json
import asyncio
from typing import List, Dict, Any, Optional, Union
from aiohttp import ClientSession


async def fetch_url(url: str, session: ClientSession) -> Optional[Dict[str, Any]]:
    # logger.info(f"[Info] Fetch {str(url)}")
    response = await session.request(method="GET", url=url)
    if response.status != 200:
        return None
    text = await response.text()
    # logger.info(f"[Info] {str(url)} responded with status code {response.status}")
    return json.loads(text)


async def fetch_urls(urls: List[str]) -> List[Union[Dict[str, Any], None]]:
    """
    Usage:
        output = asyncio.run(fetch_urls(urls=urls))
    """
    async with ClientSession() as session:
        tasks = list(fetch_url(url=url, session=session) for url in urls)
        data_dict = await asyncio.gather(*tasks)
    return data_dict
