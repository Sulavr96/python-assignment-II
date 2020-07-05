def binary_search(num_list, search_value):
    high_value_index = len(num_list) - 1
    low_value_index = 0

    while low_value_index <= high_value_index:
        mid_value_index = (high_value_index + low_value_index) // 2

        if num_list[mid_value_index] < search_value:
            low_value_index = mid_value_index + 1
        elif num_list[mid_value_index] > search_value:
            high_value_index = mid_value_index - 1
        else:
            return mid_value_index

    return -1


sorted_num_list = sorted([4, 5, 6, 2, 1, 8, 3])
search_item = int(input("Enter the number you want to search: "))

search_index = binary_search(sorted_num_list, search_item)

if search_index != -1:
    print("Value found at index: ", search_index)

else:
    print("Value not found")
