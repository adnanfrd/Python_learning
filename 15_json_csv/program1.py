import json
data = {"name": "Adnan", "age": 25}
with open("user.json", "w") as f:
    json.dump(data, f)
with open("user.json") as f:
    loaded = json.load(f)
    print(loaded)
