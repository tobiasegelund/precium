from typing import Dict, Any, List

from .item import NemligItemStatic, NemligItemPrice

# TODO: Handle other companies


def create_static_items(resp_data: List[Dict[str, Any]]):
    l = list()
    for resp in resp_data:
        if resp is not None:
            l.append(NemligItemStatic.new(**resp))

    return l


def create_price_items(resp_data: List[Dict[str, Any]]):
    l = list()
    for resp in resp_data:
        if resp is not None:
            l.append(NemligItemPrice.new(**resp))

    return l
