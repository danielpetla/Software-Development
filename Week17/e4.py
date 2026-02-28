import csv
import json
from pathlib import Path

students = []

with Path("./grades.csv").open("rt") as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header

    for row in reader:
        student = {
            "first name": row[1],
            "last name": row[0],
            "grade": row[2],
            "scores": {
                "tests": [
                    float(row[3]),
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                ],
                "final": float(row[7])
            }
        }

        students.append(student)

# Print formmated json
print(json.dumps(students, indent=4))
