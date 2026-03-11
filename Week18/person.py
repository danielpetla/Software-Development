import csv
from pathlib import Path

class Person:
    def __init__(self, name, date, country):
        self.name = name
        self.date = date
        self.country = country

    def __str__(self):
        """Formats the object nicely when printed"""
        return f"{self.name} | DOB: {self.date} | Country {self.country}"









def main():
    people_list = []

    with Path("./persons.csv").open("rt") as f:
        rows = csv.reader(f)

        header = next(rows)  # skipping header

        for row in rows:

            # Name
            name = row[0]

            # Date of birth
            date = row[1]

            # Country
            country = row[2]

            new_person = Person(name, date, country)
            people_list.append(new_person)

    for person in people_list:
        print(person)

if __name__ == "__main__":
    main()
