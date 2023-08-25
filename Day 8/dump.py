pet = {
    "name": "pascal",
    "age": 34
}

with open(r"C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 8\pet.json", "w") as pet_file:
    #conversion from dict to  str
    pet_json = json.dumps(pet)
    pet_file.write(pet_json)
    print("file has been created!")