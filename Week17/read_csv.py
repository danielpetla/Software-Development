import csv
from pathlib import Path

with Path("./grades.csv").open("rt") as f:
    rows = f.readlines() # TODO Replace with csv reader

for row in rows:
    print(row)
