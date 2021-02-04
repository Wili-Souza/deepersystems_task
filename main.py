import json

initial_json = json.load(open("source_file_2.json", "r"))

managers = []
watchers = []

final_data_m = []
final_data_w = []

for project in initial_json:
    for manager in project["managers"]:
        if manager not in managers:
            managers.append(manager)
    for watcher in project["watchers"]:
        if watcher not in watchers:
            watchers.append(watcher)

for m in managers:
    project_names = []

    for project in initial_json:
        if m in project["managers"]:
            project_names.append({"name": project["name"], "p": project["priority"]})
    
    ordered_names = sorted(project_names, key= lambda k: k["p"])
    just_names = [x["name"] for x in ordered_names]

    final_data_m.append({m: [*just_names]})



for w in watchers:
    project_names = []

    for project in initial_json:
        if w in project["watchers"]:
            project_names.append({"name": project["name"], "p": project["priority"]})

    ordered_names = sorted(project_names, key= lambda k: k["p"])
    just_names = [x["name"] for x in ordered_names]

    final_data_w.append({w: [*just_names]})

with open("final_data_w.json", "w") as file:
    json.dump(final_data_w, file)

with open("final_data_m.json", "w") as file:
    json.dump(final_data_m, file)
