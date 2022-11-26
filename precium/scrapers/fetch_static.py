import asyncio
from typing import List

from precium.producers import kafka_producer as producer
from precium.utils.asyncs import bulk_collect
from precium.utils.env import load_env_api

TOPIC = "static"


def scrape_static(company: str, uid_range: List[int]):
    """Scrape static data - It can be used as to search the number of uid a company has

    The uid_range allows to search in a different space in the future if new items have been added

    Args:
        company, str: Company name
        uid_range, List[int]: The defined minimum and maximum uid to scrape.
    """

    if (mask := len(uid_range)) != 2:
        raise ValueError(
            f"{mask} values entered in uid_range. Only two values are allowed - a mininum and maximum value"
        )
    api = load_env_api(company=company)
    urls = list(api + str(uid) for uid in range(*uid_range))

    output = asyncio.run(bulk_collect(urls=urls, topic=TOPIC, producer=producer))
    return output


def main():
    resp_data = scrape_static(company="nemlig", uid_range=[5012332, 5012340])
    if resp_data is None:
        raise ValueError()


if __name__ == "__main__":
    main()
