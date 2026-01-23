line = input().replace("O", "0").replace("l", "1").split()
s = 0
for n in line: # Line is a string and n is each character
    print(n, end=" ") # Prints each element on the same line, separated by spaces
    s += int(n) # Converts n to an integer and adds it to s
print()
print(f"Average: {s / len(line)}")