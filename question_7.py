my_friend_list = [('Hari', 'Thapa', '21'), ('Shyam', 'Gupta', 'none'), ('Dipak', 'Kc', '25'),
                  ('Anju', 'Bhatta', '28'), ('Sabin', 'Poudel', 'none'), ('Prabin', 'Shakya', '15')]

sum_of_known_age = 0
number_of_known_age = 0

for friend in my_friend_list:
    friends_age = friend[-1]
    if friends_age != 'none':
        sum_of_known_age += int(friends_age)
        number_of_known_age += 1

average_age = sum_of_known_age // number_of_known_age
print("The average age is", average_age)

for friend in my_friend_list:
    friends_full_name = friend[0] + " " + friend[1]
    friends_age = friend[-1]

    if friends_age != 'none':
        if int(friends_age) > average_age:
            print("{0}: Old ". format(friends_full_name))
        else:
            print("{0}: Young".format(friends_full_name))
