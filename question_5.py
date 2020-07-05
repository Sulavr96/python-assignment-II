person1 = ("Sulav", "Rayamajhi", 23)

people = [person1]

person2 = ("Ram", "Bahadur", 24)
person3 = ("Laxman", "Kumar", 21)
person4 = ("Sita", "Thapa", 25)

people.append(person2)
people.append(person3)
people.append(person4)

print("Sorted by first name:")
print(sorted(people, key=lambda person: person[0]))

print("Sorted by last name:")
print(sorted(people, key=lambda person: person[1]))

print("Sorted by age:")
print(sorted(people, key=lambda person: person[0]))
