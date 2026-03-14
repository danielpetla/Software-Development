from pathlib import Path
import csv

print("Opening file for reading")
with Path("grades.csv").open("rt") as f:
	students = list(csv.DictReader(f))
print(f"Read {len(students)} student from file")

print("Computing averages")
final_scores = [float(s["Final"]) for s in students]
print(f"Average: {sum(final_scores) / len(final_scores)}")

better_than_60 = [s for s in students if float(s["Test4"]) > 60]
print(f"Better than 60%: {', '.join(s['Firstname'] + ' ' + s['Lastname'] for s in students)}")
print()

def is_better_b(grade):
	return grade in {"A+", "A", "A-", "B+", "B", "B-"}

tests = [f"Test{i}" for i in range(1, 5)]

print("B- or better:")
for s in students:
	if not is_better_b(s["Grade"]):
        print(f"{s} worse than B-")
		continue
	print(f"  {s['Firstname']} {s['Lastname']}: {' '.join(s[t] for t in tests)} {s['Final']}")

print("Opening output file for writing")
with Path("out.csv").open("wt") as f:
	writer = csv.writer(f)
	writer.writerow(["Name", "Average", "Best"])
	for s in students:
		average = sum(float(s[t]) for t in tests) / len(tests)
		best = max(tests, key=s.__getitem__)
		writer.writerow([f"{s['Firstname']} {s['Lastname']}", average, best])
print("Done writing")
