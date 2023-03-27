from src.pre_built.sorting import sort_by


mock_jobs = [
    {"date_posted": "2021-03-27", 'max_salary': 10000, 'min_salary': 1500},
    {"date_posted": "2023-03-27", 'max_salary': 2000, 'min_salary': 1000},
    {"date_posted": "2022-03-27", 'max_salary': 1000, 'min_salary': 2000},
]


mock_jobs_by_min = [
    {"date_posted": "2023-03-27", 'max_salary': 4000, 'min_salary': 1000},
    {"date_posted": "2021-03-27", 'max_salary': 10000, 'min_salary': 1500},
    {"date_posted": "2022-03-27", 'max_salary': 3000, 'min_salary': 2000},
]


mock_jobs_by_date = [
    {"date_posted": "2023-03-27", 'max_salary': 4000, 'min_salary': 1000},
    {"date_posted": "2022-03-27", 'max_salary': 3000, 'min_salary': 2500},
    {"date_posted": "2021-03-27", 'max_salary': 10000, 'min_salary': 2000},
]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == mock_jobs

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == mock_jobs_by_min

    sort_by(mock_jobs, "date_posted")
    assert mock_jobs == mock_jobs_by_date
