import pytest
import time


@pytest.fixture()
def print_start_end_tests():
    start = time.time()
    return f"--- %s seconds ---" % (time.time() - start)


@pytest.fixture
def get_user_name():
    name = "Ekaterina"
    return name


@pytest.fixture
def get_second_name(request):
    request.cls.second_name = "Karas"
