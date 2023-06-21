# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# Здесь пишем код
test_file = open("test_file/task1_data.txt", 'r+', encoding='utf-8')
lines = test_file.readlines()


def get_arr_with_text_without_integers(read_lines):
    arr = []
    for line in read_lines:
        result = ''.join(i for i in line if not i.isdigit())
        arr.append(result)
    return arr


def create_new_file(text):
    my_file = open("test_file/task1_answer.txt", "w+", encoding='utf-8')
    for t in text:
        my_file.write(t)
    my_file.close()


new_array = get_arr_with_text_without_integers(lines)
create_new_file(new_array)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
