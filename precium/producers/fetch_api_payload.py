import asyncio
from typing import List

from precium.brokers import kafka_producer as producer
from precium.entities.enums import Company
from precium.utils.asyncs import bulk_collect
from precium.utils.env import load_env_api

COMPANY = Company.nemlig
API = load_env_api(company=COMPANY)
DEBUG = True


def fetch_api_payload(uid_range: List[int]) -> None:
    """Scrape static of items

    The uid_range allows to search in a different space in the future, e.g. if new items are added

    Args:
        uid_range, List[int]: The defined range (minimum and maximum) uids to scrape.

    Returns:
        None - Everything is sent to brokers
    """

    if (mask := len(uid_range)) != 2:
        raise ValueError(
            f"{mask} values entered in uid_range. Only two values are allowed - a mininum and maximum value"
        )
    urls = list(API + str(uid) for uid in range(*uid_range))

    asyncio.run(
        bulk_collect(urls=urls, company=COMPANY, producer=producer, debug=DEBUG)
    )


if __name__ == "__main__":
    fetch_api_payload(uid_range=[5012332, 5012340])
