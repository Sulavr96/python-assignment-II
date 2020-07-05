my_friend_list = []

id_before_append = id(my_friend_list)
print("id before append: ", id_before_append)
print("appending.........")
my_friend_list.append("Ram")
my_friend_list.append("Rita")
my_friend_list.append("Gita")
my_friend_list.append("Hari")

id_after_append = id(my_friend_list)
print("id after append: ", id_after_append)

if id_before_append == id_after_append:
    print("The ids are same")
else:
    print("The ids are changed")

print("\n")

sorted_my_friend_list = sorted(my_friend_list)

print("First item after sort: ", sorted_my_friend_list[0])
print("Second item after sort: ", sorted_my_friend_list[1])
