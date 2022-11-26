import asyncio
from typing import List

from precium.producers import kafka_producer as producer
from precium.utils.asyncs import bulk_collect_data
from precium.utils.env import load_env_api

TOPIC = "static"


def scrape_static(company: str, uid_interval: List[int]):
    """Scrape static data - It can be used as to search the number of uid a company has

    The uid_interval allows to search in a different space in the future if new items have been added

    Args:
        company, str: Company name
        uid_interval, List[int]: The defined minimum and maximum uid to scrape.
    """

    if (mask := len(uid_interval)) != 2:
        raise ValueError(
            f"{mask} values entered in uid_interval. Only two values are allowed - a mininum and maximum value"
        )
    api = load_env_api(company=company)
    urls = list(api + str(uid) for uid in range(*uid_interval))

    output = asyncio.run(bulk_collect_data(urls=urls, topic=TOPIC, producer=producer))
    return output


def main():
    resp_data = scrape_static(company="nemlig", uid_interval=[5012332, 5012340])
    if resp_data is None:
        raise ValueError()


if __name__ == "__main__":
    main()
