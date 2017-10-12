import re

with open("sample.txt") as file:
    lines = file.read()

def add_words_to_dictionary(lines):
    words = re.sub(r"[^a-zA-Z\s]", "", lines).lower().split()

    global word_dict
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

add_words_to_dictionary(lines)

def sort_dictionary(word_dict):
    sorted_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for word, number in sorted_list[:20]:
        print(word + ": " + str(number))

sort_dictionary(word_dict)
