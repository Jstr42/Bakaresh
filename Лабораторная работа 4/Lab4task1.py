import json


def task() -> float:
    with open('input.json', mode='r') as file:
        data = json.load(file)

    total = sum(entry["score"] * entry["weight"] for entry in data)

    return round(total, 3)


print(task())