import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    jobs_reader = read(path)
    job_type = set()

    for job in jobs_reader:
        job_type.add(job["job_type"])

    return job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
