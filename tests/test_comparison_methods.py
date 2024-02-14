from src.comparison_methods import Vacancy


def test_get_vacancy_list(new_file):
    vacancy = Vacancy.get_vacancy_list(new_file, 'Диксон', 50000)
    vacancy2 = Vacancy.get_vacancy_list(new_file, 'Диксон', 0)
    false_expected = vacancy < vacancy2
    assert false_expected == False
    assert len(vacancy) == 4
    assert len(vacancy[:2]) == 2