import csv


# функция поска ученика по id проекта
def search(iid, data):
    for stroka in data:
        if stroka[2] == iid:
            return stroka


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=','))

    # вывод данных по id проекта, пока не будет введено СТОП
    iid = input()
    while iid != 'СТОП':
        stroka = search(iid, data)
        if stroka == None:
            print('Ничего не найдено')
        else:
            print(f'Проект № {iid} делал: {stroka[1]}, он(а) получил(а) оценку - {stroka[-1]}')
        iid = input()
