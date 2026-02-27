import csv
from pathlib import Path

with Path("<put correct name here>").open("<put correct code here>") as f:
    rows = f.readlines() # TODO Replace with csv reader

for row in rows:
    print(row)
