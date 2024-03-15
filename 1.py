import csv


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as file, \
        open('students_new.csv', 'w', encoding='utf-8', newline='') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')
    print(data[1])

    # ищем необходимого ученика
    chel = 'Хадаров Владимир'
    a = []
    for stroka in data[1:]:
        if chel in stroka[1]:
            print(f'Ты получил: {stroka[4]}, за проект - {stroka[2]}')
        if stroka[4] != 'None':
            a.append(int(stroka[4]))

    # ищем среднее
    sred = sum(a) / len(a)
    sred = round(sred, 3)

    # заполняем файл students_new.csv
    res.writerow(data[0])
    for stroka in data[1:]:
        if stroka[4] == 'None':
            stroka[4] = sred
        res.writerow(stroka)

        # if stroka[4] != 'None':
        #     res.writerow(stroka)
        # else:
        #     stroka[4] = sred
        #     res.writerow(stroka)
