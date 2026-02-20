import pathlib
from collections import Counter

# Change this to "text" for the full book
file_name = "text_excerpt.txt"

# Do not modify this part
with (pathlib.Path(__file__).parent / file_name).open("rt", encoding="utf-8") as f:
    text = f.read()

print(text)

texT = text.lower()  # formatting everything to lower case

# counting the apperrance of the words and chars
count = 0
le = Counter()
c = Counter()
for words in texT.split():
    c[words] += 1
    for char in words:
        count += 1
        le[char] += 1

# printing the 20 most used words and their total usage
for key, value in c.most_common(20):
    print(f"'{key}' appears {value} times")

print()  # printing empty line

# printing the 20 most used chars and their percentage of use
for k, v in le.most_common(20):
    percentage = (v/count)*100
    print(f"'{k}' appears {percentage:.2f}%")
