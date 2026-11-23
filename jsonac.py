import json

 

task = {"description": "Study Python", "done": False}

with open("task.json", "w", encoding="utf-8") as file:

    json.dump(task, file, indent=2)

 

with open("task.json", "r", encoding="utf-8") as file:

    restored = json.load(file)

print(restored["description"])