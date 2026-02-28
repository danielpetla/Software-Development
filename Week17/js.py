import json
from pathlib import Path

with Path("./users.json").open("rt") as f:
    data = json.load(f)

    total = []
    for person, info in data.items():
        if info["online"] is True:
            print(f'online: {info["username"]}')

        total.append(info["followers"])

    avg = sum(total)/len(total)

    print(f"Avrage followers: {avg}")
