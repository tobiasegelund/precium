import os


def load_env_api(company: str) -> str:
    """Load API defined as environmental variables"""
    mapping = {"nemlig": "NEMLIG_API"}

    try:
        env_name = mapping.get(company)
    except KeyError:
        raise ValueError(f"{company} not among the options {mapping.keys()}")

    api = os.environ[env_name]

    if api == "":
        raise ValueError(f"Environmental variable {env_name} is undefined")
    return api
