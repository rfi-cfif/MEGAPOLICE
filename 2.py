import csv


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=','))

    print(data[1])

    #
    
