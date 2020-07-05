import csv


def create_csv(file_name, people_list):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "address", "age"])

        for people_tuple in people_list:
            writer.writerow(list(people_tuple))

    print("CSV file created")


file_name = input("Enter a file name: ")
people_list = [("Ram", "Pulchowk, Lalitpur", 20), ("John", "Salt lake city", 23),
               ("George", "New York", 24)]

create_csv(file_name, people_list)
