import csv


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=','))[1:]

    # data = sorted(data, key=lambda x: -int(x[4]) if x[4] != 'None' else 0)

    for i in range(1, len(data)):
        j = i - 1
        data[i][4] = data[i][4] if data[i][4] != 'None' else 0

        while j >= 0 and int(data[j + 1][4]) > int(data[j][4]):
            data[j + 1], data[j] = data[j], data[j + 1]
            j -= 1

    # for i in data:
    #     print(*i)
    grade = 10
    n = 1

    for stroka in data:
        if stroka[3][:2] == str(grade):
            surname, name, fath = stroka[1].split()
            print(f'{n} место: {name[0]}. {surname}')
            n += 1

        if n == 4:
            break