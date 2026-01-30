s = input("Please enter a string: ")
words = s.split()
print(words)

new_list = []

for index, word in enumerate(words):
    if len(word) > index:
        new_list.append(word)

sentence = " ".join(new_list)
print(sentence)
