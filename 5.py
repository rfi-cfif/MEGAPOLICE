import csv


# словарь символов для хэш
alf = sorted(' ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
dict = {alf[i]: i + 1 for i in range(len(alf))}
print(dict)


# функция задаёт строке уникальный хэш
# s - входная строка, возвращает уникальный хэш этой строки
def hash(s):
    p = 71
    m = 10 ** 9 + 9
    hash_value = 0
    i = 0
    for char in s:
        hash_value += dict[char] * p ** i
        i += 1
    return int(hash_value % m)


# считываем файл students.csv и создаём файл students_with_hash.csv
with open('students.csv', encoding='utf-8') as file, \
    open('students_with_hash.csv', 'w', encoding='utf-8',newline='') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

    # заполняем файл строками из исходного, заменяя id на хэш
    res.writerow(data[0])
    for stroka in data[1:]:
        fio = stroka[1]
        h = hash(fio)
        stroka[0] = h
        res.writerow(stroka)
