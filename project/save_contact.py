import json
import os 





import json
import os

working_directory = os.getcwd()
project_path = os.path.join(working_directory, "project")

# get only json files
list_of_all_files = os.listdir(project_path)
list_of_json_files = []
for file in list_of_all_files:
    if file.endswith(".json"):
        path = os.path.join(project_path, file)
        list_of_json_files.apend(path)

print(list_of_json_files)

#get all the content from the json files

contacts = {}
for json_file in list_of_json_files:
    with open(json_file, 'r') as f:
        content = f.read
        contact = json.loads(content)
        contacts.append(contacts)

print(contacts)