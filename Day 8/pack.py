import math
print(math.cos(34))


from math import cos
print(cos(34))


import json

with open(
    r'C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 8\person.json', 'r'
) as json_file:
    content = json_file.read()
# conversation from string to dictionary
    person = json.loads(content)
    print(person)

# absolute path: C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 8\person.json ---> right click file name on the left + copy path.
# relative path: person.json  ----> right click file name on the left + copy relative path.