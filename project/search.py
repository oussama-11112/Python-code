# search

search_input = input("what are you searching for?: ")
result =  {}

for contact in contacts:
    if search_input in contact["name"]:
        result = contact

print("the result of your search: ", search_input)
if(len(result)>0):
    print(result)
else:
    print("contact not found!")