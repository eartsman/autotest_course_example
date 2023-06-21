# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
from typing import TextIO


# Здесь пишем код
def read_file(path_to_file):
    with open(path_to_file, 'r+', encoding='utf-8') as file:
        lines = file.read().strip().splitlines()
        return lines


def get_total_sum_prices(lines_list):
    arr = []
    count_sums = []
    for line in lines_list:
        if line != '':
            arr.append(int(line))
        else:
            summa = sum(arr)
            count_sums.append(summa)
            arr.clear()
    t = sorted(count_sums, reverse=True)
    total_sum = sum(t[0:3])
    return total_sum


lines = read_file('test_file/task_3.txt')
three_most_expensive_purchases = get_total_sum_prices(lines)

assert three_most_expensive_purchases == 202346
