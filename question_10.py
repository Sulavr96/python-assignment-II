def camel_case_converter(camel_case_string, separator):
    converted_string = ''
    camel_case_word_length = len(camel_case_string)

    for i in range(camel_case_word_length):
        char = camel_case_string[i]

        if char.isupper():
            if i == 0:
                converted_string += char.lower()
            else:
                converted_string += separator + char.lower()
        else:
            converted_string += char

    return converted_string


user_camel_case_word = input("Enter a camel case string you want to convert: ")
string_separator = input("Enter a separator: ")

print("The converted word is: ", camel_case_converter(user_camel_case_word, string_separator))
