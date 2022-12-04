import os
from ..entities.enums import Company


def load_env_api(company: Company) -> str:
    """Load API defined as environmental variables"""
    mapping = {Company.nemlig: "NEMLIG_API"}

    try:
        env_name = mapping.get(company)
    except KeyError:
        raise ValueError(f"{company} not among the options {mapping.keys()}")

    api = os.environ[env_name]

    if api == "":
        raise ValueError(f"Environmental variable {env_name} is undefined")
    return api
