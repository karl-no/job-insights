from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries_reader = read(path)
    industries = set()

    for industry in industries_reader:
        if len(industry["industry"]) > 0:
            industries.add(industry["industry"])

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industries = [job for job in jobs if job["industry"] == industry]
    return industries
