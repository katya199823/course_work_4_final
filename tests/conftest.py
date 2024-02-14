import json

import pytest

from config import DATA_TEST
from src.get_data import GetApiHh
from src.json_saver import JsonSaver


@pytest.fixture
def fixture_class_get_hh_valid():
    return GetApiHh().get_vacancy_from_api('python')


@pytest.fixture
def fixture_class_get_hh_negative():
    return GetApiHh().get_vacancy_from_api("1")


@pytest.fixture
def fixture_class_json_saver():
    return JsonSaver()

@pytest.fixture
def fixture_class_list():
    json_saver = JsonSaver()
    json_saver.save_file([{'name': 'Volodya'}])
    return json_saver


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)