import csv


def read_csv():
    people_list = []
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        iter_reader = iter(reader)
        next(iter_reader)

        for row in iter_reader:
            people_dict = {'name': row[0], 'address': row[1], 'age': row[2]}
            people_list.append(people_dict)

    print(people_list)


read_csv()
