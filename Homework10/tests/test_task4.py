# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures('get_second_name')
class TestUser:

    def test_username(self, get_user_name):
        assert get_user_name == 'Ekaterina', 'имя пользователя не совпало'

    def test_second_name(self):
        assert self.second_name == 'Karas', 'фамилия пользователя не совпала'