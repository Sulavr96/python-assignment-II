def is_palindrome(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True


user_input_word = input("Enter a word:")

if is_palindrome(user_input_word):
    print("The word is palindrome")
else:
    print("The word is not palindrome")
