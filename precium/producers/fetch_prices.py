import asyncio
from typing import List

from precium.utils.asyncs import bulk_collect
from precium.utils.env import load_env_api

TOPIC = "price"
API = load_env_api(company="nemlig")


def scrape_price(uid: int, company: str):
    pass
