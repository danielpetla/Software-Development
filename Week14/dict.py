# Part 1
mapping = {
    "hello": "Olá",
    "goodbye": "Tchau",
    "university": "Universidade",
    "computer": "Computador",
    "dictionary": "Dicionário",
    "love": "Amor"
}

st = input("Please insert a string:")

missing = []
translated_words = []

for word in st.split():
    key = word.lower()          # normalize for lookup
    if key in mapping:
        translated_words.append(mapping[key])
    else:
        translated_words.append(word)
        missing.append(word)

result = " ".join(translated_words)

print("Translation =", result)
print("Missing words:", " ".join(missing))

# ----------------------------------------------------------------

# Part 2
st2 = "hallo hallllouh aolh xhallo"

words = {}

for word in st2.split():
    # key = word.lower()  # for grouping normal and without vowels
    key = frozenset(c for c in word.lower() if c not in "aeiou")  # for grouping based on consonants

#    for v in "aeiou":  # for grouping without vowels
#        key = key.replace(v, "")

    if key not in words:
        words[key] = set()  # creating a key
    words[key].add(word)  # adding the variants related to the key

print(st2)
# print result
for i, (key, variants) in enumerate(words.items(), start=1):  # printing each variants of the key
    print(i, " ".join(variants))
