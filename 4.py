import random
import csv


# функция создания логина в формате Фамилия_ИО
def create_login(s):
    fam, name, fath = s.split()
    login = f'{fam}_{name[0]}{fath[0]}'
    return login


# функция генерации пароля
def create_password():
    alf = 'qwertyuiopasdfghjklzxcvbnm'
    ALF = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    digit = '1234567890'
    alf0 = alf + ALF + digit
    while True:
        password = ''.join(random.choice(alf0) for i in range(8))
        k1 = sum([1 for i in alf])
        k2 = sum([1 for i in ALF])
        k3 = sum([1 for i in digit])
        if k1 * k2 * k3 != 0:
            return password


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as file, \
    open('students_password', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

    data[0].append('login')
    data[0].append('password')
    res.writerow(data[0])
    for stroka in data[1:]:
        stroka.append(create_login(stroka[1]))
        stroka.append(create_password())
        res.writerow(stroka)
