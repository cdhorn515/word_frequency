import re

with open("sample.txt") as file:
    lines = file.read()

def add_words_to_dictionary(lines):
    words = re.sub(r"[^a-zA-Z\s]", "", lines).lower().split(" ")

    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

print(add_words_to_dictionary(lines))
