import pathlib
import sys

# Change this to "text" for the full book
file_name = "text.txt"

# Do not modify this part
with pathlib.Path(file_name).open("rt", encoding="utf-8") as f:
    text = f.readlines()


# Find all words that appear
words = set(w.lower() for line in text for w in line.split())

# Count how often each appears
counts = {}
for line in text:
    for w in line.split():
        word = w.lower()
        # go to the key (word) and increment the value tha is related to it
        counts[word] = counts.get(word, 0) + 1
# Print out the counts
for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    if value > 4:
        print(f"{value}: {key}")
