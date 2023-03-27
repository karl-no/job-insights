from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary_reader = read(path)
    max_salary = []

    for salary in salary_reader:
        if salary["max_salary"] and salary["max_salary"] != "invalid":
            max_salary.append(int(salary["max_salary"]))

    return max(max_salary)


def get_min_salary(path: str) -> int:
    salary_reader = read(path)
    min_salary = []

    for salary in salary_reader:
        if salary["min_salary"] and salary["min_salary"] != "invalid":
            min_salary.append(int(salary["min_salary"]))

    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError
    else:
        if min_salary > max_salary:
            raise ValueError
        return max_salary >= salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            continue
            # pass
    return salary_range
