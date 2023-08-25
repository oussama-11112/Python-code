pets = ["cat", "dog", "rabbit", "bird", "fish", "turtle"]

print("before delete:\n")
print(pets)

print ("\n\nAfter delete:\n")
del pets[0]
del pets[-1]
del pets[pets.index("bird")] = "mouse"
# del pets[pets.index("bird")]
print(pets)