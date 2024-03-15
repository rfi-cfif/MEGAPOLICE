import csv


# считываем файл students.csv
with open('students.csv', encoding='utf-8') as file, open('students_password.csv', 'w', encoding='utf-8', newline='') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

    print(data[:5])
