def process(lines):
    cost = 0
    largest_volume = 0
    largest_part_name = ""
    materials = []
    largest_expense = 0
    pricy = ""
    cost_more = []

    for line in lines:
        sep = line.split()

        # cost
        cost += float(sep[5])

        # volume
        volume = 1
        for d in sep[3].split("x"):
            volume *= float(d)


        # comparing the volumes
        if volume > largest_volume:
            largest_volume = volume
            largest_part_name = sep[0]

        # checking if steel
        material = sep[4]
        if material == 'Steel':
            materials.append(sep[0])

        # expensive
        unit = float(sep[5])
        expense = unit * float(sep[2])

        # comparing expense
        if expense > largest_expense:
            largest_expense = expense
            pricy = sep[0]

        # checking for €100
        if expense >= 100:
            cost_more.append(sep[0])

    print("Total cost:", cost)
    print("Largest part:", largest_part_name)
    print("Steel Materials:", materials)
    print("The most expensive part:", pricy)
    print("Cost more than €100:", cost_more)

# ---------------------------------------------------------------------------------------------------

# Do not modify below
if __name__ == "__main__":
    import sys
    import pathlib

    if len(sys.argv) != 2:
        sys.exit("Usage: python production.py <dataset> (try python production.py data_1.txt)")

    data = pathlib.Path(sys.argv[0]).parent / sys.argv[1]
    if not data.is_file():
        sys.exit(f"{data} is not a file")

    with data.open("rt") as f:
        lines = [l.strip() for l in f.read().splitlines() if l.strip()]

    process(lines)
