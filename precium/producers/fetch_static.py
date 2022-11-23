from precium.items import create_static_items
from precium.scrapers import scrape_static


def main():
    resp_data = scrape_static(company="nemlig", uid_interval=[5012332, 5012340])
    if resp_data is None:
        raise ValueError()
    items = create_static_items(resp_data=resp_data)


if __name__ == "__main__":
    main()
