names = ["farah", "anas","rawane"] # original

names.append("chahd")
names[3] = "mohamed"

print (names) #changeable



pets = ("cat", "dog", "hamster") #immutable
print(pets[2]) #hamster
#different between list and arrays
print("the first element is", pets[0])



list_of_pets = ["cat", "dog", "Hamster"]
list_of_pets[-1] = "chicken"
tuple_of_pets = ("cat", "cat", "dog", "Hamster")
#tuple_of_pets[-1] = 'chicken' #wrong
print("the position of hamster is: ", tuple_of_pets.index("Hamster"))


tuple_of_nots = (12, 20, 14, 20, 4, 13, 20)
print(tuple_of_nots.count(20))