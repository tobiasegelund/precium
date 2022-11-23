import asyncio
from typing import List
from kafka.producer import KafkaProducer

from precium.utils.asyncs import fetch_urls
from precium.utils.env import load_env_api


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

    output = asyncio.run(fetch_urls(urls=urls))
    return output


# Send values with KafkaProducer


def main():
    resp_data = scrape_static(company="nemlig", uid_interval=[5012332, 5012340])
    if resp_data is None:
        raise ValueError()


if __name__ == "__main__":
    main()
