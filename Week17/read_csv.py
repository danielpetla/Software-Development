import csv
from pathlib import Path

with Path("/Users/daniel.petla/Documents/GitHub/Software-Development/Week17/grades.csv").open("rt") as f:
    rows = f.readlines() # TODO Replace with csv reader

for row in rows:
    print(row)
