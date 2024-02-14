from abc import ABC

from src.abstract_json import AbstractJsonSaver
from src.json_saver import JsonSaver


def test_json_saver_issubclass():
    assert issubclass(JsonSaver, AbstractJsonSaver)
    assert issubclass(AbstractJsonSaver, ABC)


def test_save_file_read_file(fixture_class_json_saver):
    fixture_class_json_saver.save_file([{'name': 'Volodya'}])

    assert isinstance(fixture_class_json_saver.read_file(), list)
    assert fixture_class_json_saver.read_file() == [{'name': 'Volodya'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Volodya'}])

    assert fixture_class_list.read_file() == [{'name': 'Not Volodya'}, {'name': 'Volodya'}]

    fixture_class_list.delete_vacancy('Volodya')
    assert fixture_class_list.read_file() == [{'name': 'Not Volodya'}]
