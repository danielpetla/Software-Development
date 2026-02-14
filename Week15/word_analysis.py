import pathlib
import sys

# Change this to "text" for the full book
file_name = "text.txt"

# Do not modify this part
with pathlib.Path(file_name).open("rt", encoding="utf-8") as f:
    text = f.readlines()

# Find all words that appear
words = set(w.lower() for line in text for w in line.split())

# ---------

# Count how often each word appears
counts = {}
for line in text:
    for w in line.split():
        word = w.lower()
        # go to the key (word) and increment the value that is related to it
        counts[word] = counts.get(word, 0) + 1
# Print out the counts
for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    if value > 4:
        print(f"{value}: {key}")

# ---------
# Finds all the characters in the book
letters = (le.lower() for line in text for w in line.split() for le in list(w))

# Counting how often each char appears
counts_l = {}
for line in text:
    for w in line.split():
        for le in list(w.lower()):
            letter = le.lower()
            # go to the key (letter) and increment the value that is related to it
            counts_l[letter] = counts_l.get(letter, 0) + 1

total = 0
for c, v in counts_l.items():
    total += v

for c, v in counts_l.items():
    avg = (v/total) * 100
    counts_l[c] = avg

for key, value in sorted(counts_l.items(), key=lambda item: item[1], reverse=True):
    if value >= 0.01:
        print(f"{value:.2f}%: {key}")
