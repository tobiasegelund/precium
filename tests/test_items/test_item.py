import pytest
from attrs import asdict

from precium.items.item import NemligItemStatic, NemligItemPrice


def test_item_static_class():
    resp = {
        "Id": 1,
        "Text": "And",
        "Brand": "RandomBrand",
        "Category": "Food",
        "Labels": "Frozen",
        "ProductMainGroupName": "Meat",
        "ProductSubGroupName": "Duck",
        "UnitPriceLabel": "DKK/kg",
    }

    exp = {
        "uid": 1,
        "description": "And",
        "brand": "RandomBrand",
        "category": "Food",
        "tags": "Frozen",
        "product_main_group": "Meat",
        "product_sub_group": "Duck",
        "unit_price_label": "DKK/kg",
    }

    item = NemligItemStatic.new(resp=resp)
    assert asdict(item) == exp


@pytest.mark.parametrize(
    "resp, exp",
    [
        (
            {
                "Id": 1,
                "Price": 50.0,
                "UnitPriceCalc": 25.0,
                "Campaign": {
                    "CampaignPrice": 30.0,
                    "CampaignUnitPrice": 15.0,
                    "DiscountSavings": 20.0,
                },
            },
            {
                "uid": 1,
                "base_price": 50.0,
                "unit_price": 25.0,
                "current_price": 30.0,
                "current_unit_price": 15.0,
                "discount": 20.0,
            },
        ),
        (
            {
                "Id": 1,
                "Price": 50.0,
                "UnitPriceCalc": 25.0,
            },
            {
                "uid": 1,
                "base_price": 50.0,
                "unit_price": 25.0,
                "current_price": 50.0,
                "current_unit_price": 25.0,
                "discount": None,
            },
        ),
    ],
)
def test_item_price_class(resp, exp):
    item = NemligItemPrice.new(resp=resp)
    assert asdict(item) == exp
