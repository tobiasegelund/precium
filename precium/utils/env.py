import os
from .enums import Company


def load_env_api(company: Company) -> str:
    """Load API defined as environmental variables"""
    mapping = {"nemlig.com": "NEMLIG_API"}

    try:
        env_name = mapping.get(company.value)
    except KeyError:
        raise ValueError(f"{company} not among the options {mapping.keys()}")

    api = os.environ[env_name]

    if api == "":
        raise ValueError(f"Environmental variable {env_name} is undefined")
    return api
