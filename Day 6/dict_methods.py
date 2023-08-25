fruit = {
    "name": "orange",
    "weight": "10kg"
    "score": 5
}

fruit.pop("score")
fruit.update({"quality": "good"}) #update
fruit.update({"name": "apple"})
print(fruit)

print("All the keys: ", fruit.keys())
print("All the values: ", fruit.values())

print(fruit.get("name"))