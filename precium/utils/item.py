import attrs
from typing import List, Dict, Any


class Item:
    uid: int = attrs.field(validator=attrs.validators.instance_of(int))
    base_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    current_price: float = attrs.field(validator=attrs.validators.instance_of(float)) # if any campaign price
    unit_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    current_unit_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    unit_price_label: float = attrs.field(validator=attrs.validators.instance_of(str))
    discount: float = attrs.field(validator=attrs.validators.instance_of(float))

    @classmethod
    def new(cls, resp: Dict[str, Any]):
        raise NotImplementedError()

@attrs.define
class ItemStatic(Item):
    uid: int = attrs.field(validator=attrs.validators.instance_of(int))
    category: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    product_main_group: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    product_sub_group: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    description: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    brand: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    tags: List[str] = attrs.field(default=[])

    def collect_static(self) -> None:
        raise NotImplementedError()


@attrs.define
class ItemPrice(Item):
    uid: int = attrs.field(validator=attrs.validators.instance_of(int))
    base_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    current_price: float = attrs.field(validator=attrs.validators.instance_of(float)) # if any campaign price
    unit_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    current_unit_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    unit_price_label: float = attrs.field(validator=attrs.validators.instance_of(str))
    discount: float = attrs.field(validator=attrs.validators.instance_of(float))

    def collect_price(self) -> None:
        raise NotImplementedError()


class NemligItemStatic(ItemStatic):
    mapping = {
        "uid": "Id",
        "description": "Text",
        "brand": "Brand",
        "category": "Category",
        "tags": "Labels",
        "product_main_group": "ProductMainGroupName",
        "product_sub_group": "ProductSubGroupName",
    }

    @classmethod
    def new(cls, resp: Dict[str, Any]):
        return cls(**resp)

    def _unpack_campaign(self, resp: Dict[str, Any]) -> Dict[str, Any]:
        return resp.get("Campaign", None)

    def collect_static(self) -> None:
        pass


class NemligItemPrice(ItemPrice):
    mapping = {
        "uid": "Id",
        "base_price": "Price",
        "unit_price": "UnitPriceCalc",
        "current_price": "CampaignPrice",
        "current_unit_price": "CampaignUnitPrice",
        "unit_price_label": "UnitPriceLabel",
        "discount": "DiscountSavings"
    }

    @classmethod
    def new(cls, resp: Dict[str, Any]):
        return cls(**resp)

    def _unpack_campaign(self, resp: Dict[str, Any]) -> Dict[str, Any]:
        return resp.get("Campaign", None)

    def collect_price(self) -> None:
        pass

class RemaItem(Item):
    pass


class BilkaItem(Item):
    pass