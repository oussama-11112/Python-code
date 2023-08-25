fruit = {
    "name": "orange",
    "weight": "10kg",
    "score": 5
}
print(fruit)
print("the name of the fruit is ", fruit["name"])
print("the weight of the fruit is ", fruit["weight"])
# dictionary ---> curly brackets -->{}
print("the size of the fruit is: ", len(fruit))

#update
fruit["name"] = "apple"
fruit["quality"] = "good"
print(fruit)

#delete
del fruit ["score"]
print(fruit)

# empty the dictionary # fruit.clear()
print(fruit)