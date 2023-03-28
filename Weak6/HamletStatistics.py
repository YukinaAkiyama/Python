import string

word_count = {}
meaningless_words = ["a", "an", "the", "of", "to", "i", "to", "in", "on", "at", "and", "it", "is", "s", "be"]
with open('hamlet.txt', encoding='utf-8') as file_obj:
    words = file_obj.read()

for i in string.punctuation:
    words = words.replace(i, " ")

words = words.split()

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    if word_count_sorted[i][0] not in meaningless_words:
        print(word_count_sorted[i])
