# TODO решите задачу
import json


def task() -> float:
    with open ('input.json', 'r') as file:
        data = json.load(file)

    return round(sum(d['score'] * d['weight'] for d in data),3)

print(task())
