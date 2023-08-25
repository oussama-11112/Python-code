
import json
# json --> dict

with open(r"C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 10\person.json", "r") as json_file:
    content = json_file.read()
    # conversion
    person_dict = json.loads(content)
    print(type(person_dict))

# update person_dict
# add email

person_dict['email'] = "ahmadmohsen@gmail.com"

with open(r"person.json", "w") as json_file:
    # conversion from dict --> str
    person_str = json.dumps(person_dict)
    json-file.write(person_str)