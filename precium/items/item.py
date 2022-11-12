import json
import attrs
from typing import List, Dict, Any, Optional

from .company import CompanyNemlig


@attrs.define(frozen=True)
class Item:
    @classmethod
    def new(cls, resp: Dict[str, Any]):
        raise NotImplementedError()

    def serialize(self):
        return json.dumps(attrs.asdict(self))


@attrs.define
class ItemStatic(Item):
    uid: int = attrs.field(validator=attrs.validators.instance_of(int))
    category: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    product_main_group: str = attrs.field(
        default="", validator=attrs.validators.instance_of(str)
    )
    product_sub_group: str = attrs.field(
        default="", validator=attrs.validators.instance_of(str)
    )
    description: str = attrs.field(
        default="", validator=attrs.validators.instance_of(str)
    )
    brand: str = attrs.field(default="", validator=attrs.validators.instance_of(str))
    tags: List[str] = attrs.field(default=[])
    unit_price_label: str = attrs.field(
        default="", validator=attrs.validators.instance_of(str)
    )


@attrs.define
class ItemPrice(Item):
    uid: int = attrs.field(validator=attrs.validators.instance_of(int))
    base_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    unit_price: float = attrs.field(validator=attrs.validators.instance_of(float))
    current_price: float = attrs.field(
        validator=attrs.validators.instance_of(float)
    )  # if any campaign price
    current_unit_price: float = attrs.field(
        validator=attrs.validators.instance_of(float)
    )
    discount: Optional[float] = attrs.field(default=None)

    def _unpack_campaign(self, resp: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError()


class NemligItemStatic(ItemStatic, CompanyNemlig):
    @classmethod
    def new(cls, resp: Dict[str, Any]):
        build_dict = {}

        for key, kw in cls.static_kw_mapping.items():
            val = resp.get(kw)
            build_dict.update({key: val})

        return cls(**build_dict)


class NemligItemPrice(ItemPrice, CompanyNemlig):
    @classmethod
    def new(cls, resp: Dict[str, Any]):
        build_dict = {}

        campaign = cls._unpack_campaign(resp=resp)
        if campaign is None:
            # If no campaign: current price = base price
            cls.prices_kw_mapping.update(
                {
                    "current_price": "Price",
                    "current_unit_price": "UnitPriceCalc",
                }
            )

        for key, kw in cls.prices_kw_mapping.items():
            val = resp.get(kw, None)
            if val is None:
                if campaign is not None:
                    val = campaign.get(kw, None)
            build_dict.update({key: val})

        return cls(**build_dict)

    @classmethod
    def _unpack_campaign(cls, resp: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return resp.get("Campaign", None)
