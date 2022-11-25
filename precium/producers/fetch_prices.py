import json
import uuid
import datetime
import asyncio
from typing import List

from kafka.producer import KafkaProducer
from aiohttp import ClientSession

from precium.utils.asyncs import get_and_send_data_async
from precium.utils.env import load_env_api

TOPIC = "price"


def scrape_price(uid: int, company: str):
    pass
