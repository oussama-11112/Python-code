pets = {"cat", "dog", "hamster"}

for position, pet in enumerate(pets):
    print("the pet ", pet, "of position of ", position)
#len
#sorted
#min
#max
print("\n\n")
pets = sorted(pets, reverse=True)
for position, pet in enumerate(pets):
    print("the pet ", pet, "of position of ", position)


numbers = {4, 55, 12}
print("the max of the numbers is: ", max(numbers))
print("the min of the numbers is: ", min(numbers))