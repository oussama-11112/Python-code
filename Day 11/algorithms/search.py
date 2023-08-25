# linear search

def search(array, item):
    position = None
    for i in range(len(array)):
        print("checking ", array[i], "and", item)
        if array[i] == item:
            position = i
            break
        
    if position == None:
        print("not found")
    else:
        print("found at position ", position)
        
        
array = [34, 54, 4, 3435, 23, 4]

item = int(input("enter a number : "))