from task_2 import all_division
import pytest

FIRST_NUMBER = 2


@pytest.mark.smoke
def test_division_on_integer():
    assert all_division(FIRST_NUMBER, 4)


@pytest.mark.smoke
def test_division_with_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(FIRST_NUMBER, 0)


@pytest.mark.smoke
def test_division_on_negative_number():
    assert all_division(FIRST_NUMBER, -3)


def test_division_on_fraction():
    assert all_division(FIRST_NUMBER, 0.3)


def test_division_on_not_number(print_start_end_tests):
    with pytest.raises(TypeError):
        print(print_start_end_tests)
        all_division(FIRST_NUMBER, 'abc')
