# flake8: noqa
import json

data = {
    "name": "Alice",
    "age": 28,
    "city": "New York"
}

with open("data/perfil/output.txt", "w") as file:
    json.dump(data, file)
