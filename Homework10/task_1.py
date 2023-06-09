# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    rnd_index = random.randint(2, 7)
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(1, 16))
    name = rand_string[:len(rand_string)//rnd_index]
    second_name = rand_string[len(rand_string)//rnd_index:]
    fio = f'{name} {second_name}'
    yield fio


#gen = generate_random_name()
#print(next(gen))
#print(next(gen))


def random_names():
    test = []
    rnd_index = random.randint(2, 7)
    while rnd_index > 0:
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(1, 16))
        name = rand_string[:len(rand_string) // rnd_index]
        second_name = rand_string[len(rand_string) // rnd_index:]
        fio = f"{name} {second_name}"
        test.append(fio)
        if rnd_index == 2:
            break
        rnd_index -= 1
    for item in test:
        yield item


try:
    random_name = random_names()
    print(next(random_name))
    print(next(random_name))
    print(next(random_name))
    print(next(random_name))
    print(next(random_name))
    print(next(random_name))
    print(next(random_name))
except Exception:
    pass



