import csv
from pathlib import Path

with Path("./grades.csv").open("rt") as f:
    rows = csv.reader(f)

    header = next(rows)  # Skiping header

    total = 0
    count = 0
    sl = {}

    for row in rows:

# Students final year avrage
        total += float(row[7])
        count += 1

# Studedents with more then 60% in the test 4
        if float(row[6]) >= 60.0:
            sl[row[1]] = row[0]

# Students with a B- or better
        grades = [float(row[i]) for i in range(3, 8)]
        avg = sum(grades) / len(grades)

        if avg >= 38.6:
            print(f"{row[1]} {row[0]}: s1: {row[3]}, s2: {row[4]}, s3: {row[5]}, s4: {row[6]}, final: {row[7]}")

    avg = total/count
    print()
    print(f"the Avrage is: {avg}")
    print()
    print(f"Students over 60% in test 4: {sl}")
