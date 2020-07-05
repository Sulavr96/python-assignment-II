paragraph = "A cat was trying to act as if it was sleeping. The man " \
            "was very devoted to god. He also had a dog. It was just " \
            "below the elbow of that man." \
            "The man was trying to study a dusty book." \

word_list = paragraph.split(" ")
word_list_length = len(word_list)

anagram_list = []

for word_1 in word_list:
    for word_2 in word_list:
        if sorted(word_1) == sorted(word_2) and word_1 != word_2:
            last_char = word_1[-1]

            if last_char == ".":
                anagram_list.append("".join(word_1.replace('.', '')))
            elif last_char == ",":
                anagram_list.append("".join(word_1.replace(',', '')))
            else:
                anagram_list.append("".join(word_1))


print("Anagram words: ", anagram_list)
