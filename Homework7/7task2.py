# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:
    def __init__(self, fio, age, subdivision='Разработка', department='', group='', sub_group=''):
        self.fio = fio
        self.age = age
        self.subdivision = subdivision
        self.department = department
        self.group = group
        self.sub_group = sub_group

    def short_name(self):
        split_fio = self.fio.split(' ')
        result = f'{split_fio[1]} {split_fio[0][0]}.'
        return result

    def path_deps(self):
        if self.subdivision != "" and self.department == "" and self.group == "" and self.sub_group == "":
            return f'{self.subdivision}'
        elif self.department == "":
            return f'{self.subdivision} --> {self.group} --> {self.sub_group}'
        elif self.group == "":
            if self.sub_group != "":
                return f'{self.subdivision} --> {self.department} --> {self.sub_group}'
            return f'{self.subdivision} --> {self.department}'
        elif self.sub_group == "":
            return f'{self.subdivision} --> {self.department} --> {self.group}'
        else:
            return f'{self.subdivision} --> {self.department} --> {self.group} --> {self.sub_group}'

    def new_salary(self):
        all_words_in_string = f'{self.subdivision}{self.department}{self.group}{self.sub_group}'
        words_dict = {}
        new_salary = 1337 * self.age
        for word in all_words_in_string:
            count_char = all_words_in_string.count(word)
            words_dict[word] = count_char
        sorted_list = sorted(words_dict.values(), reverse=True)[:3]
        counter_chars_arr_without_duplicate = list(set(words_dict.values()))
        if len(counter_chars_arr_without_duplicate) < 3:
            sum_with_duplicate = sum(sorted_list)
            return new_salary * sum_with_duplicate
        sum_chars_in_words = sum(sorted_list)
        return new_salary * sum_chars_in_words

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')