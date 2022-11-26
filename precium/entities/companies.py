from enum import Enum


class Company(Enum):
    nemlig = "nemlig.com"


class CompanyNemlig:
    COMPANY_NAME = "Nemlig.com"

    static_kw_mapping = {
        "uid": "Id",
        "description": "Text",
        "brand": "Brand",
        "category": "Category",
        "tags": "Labels",
        "product_main_group": "ProductMainGroupName",
        "product_sub_group": "ProductSubGroupName",
        "unit_price_label": "UnitPriceLabel",
    }

    prices_kw_mapping = {
        "uid": "Id",
        "base_price": "Price",
        "unit_price": "UnitPriceCalc",
        "current_price": "CampaignPrice",
        "current_unit_price": "CampaignUnitPrice",
        "discount": "DiscountSavings",
    }
