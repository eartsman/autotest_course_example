import pytest


all_test_data = [pytest.param("3+6", 9, marks=pytest.mark.smoke), ("1+1", 2), pytest.param("0+10", 11, marks=pytest.mark.skip)]


@pytest.mark.parametrize("number_input, expected_sum", all_test_data)
def test_sum_numbers(number_input, expected_sum):
    assert eval(number_input) == expected_sum, "Неверная сумма чисел!"