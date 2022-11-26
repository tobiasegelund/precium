import asyncio
from typing import List

from precium.utils.asyncs import bulk_collect_data
from precium.utils.env import load_env_api

TOPIC = "price"


def scrape_price(uid: int, company: str):
    pass
