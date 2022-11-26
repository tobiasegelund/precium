import asyncio
from typing import List

from precium.producers import kafka_producer as producer
from precium.entities.companies import Company
from precium.utils.asyncs import bulk_collect
from precium.utils.env import load_env_api

TOPIC = "static"
API = load_env_api(company=Company.nemlig)


def scrape_static(uid_range: List[int]) -> None:
    """Scrape static data - It can be used as to search the number of uid a company has

    The uid_range allows to search in a different space in the future if new items have been added

    Args:
        uid_range, List[int]: The defined minimum and maximum uid to scrape.
    """

    if (mask := len(uid_range)) != 2:
        raise ValueError(
            f"{mask} values entered in uid_range. Only two values are allowed - a mininum and maximum value"
        )
    urls = list(API + str(uid) for uid in range(*uid_range))

    asyncio.run(bulk_collect(urls=urls, topic=TOPIC, producer=producer))


if __name__ == "__main__":
    scrape_static(uid_range=[5012332, 5012340])
