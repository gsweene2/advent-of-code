# advent-of-code

[https://adventofcode.com/](https://adventofcode.com/)

## Repo Setup

```
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
# 1.2.2
```

## Run Tests

```
poetry shell
poetry install
poetry run pytest
```

## Add Dependencies

```
poetry add mypy
```

## Start a new coding day

```
poetry run python tools/new_day.py yyyy d
# poetry run python tools/new_day.py 2022 5
```
