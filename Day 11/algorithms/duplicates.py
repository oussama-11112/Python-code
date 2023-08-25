def count_duplicates(array, item):
    count = 0
    n = len(array)
    for number in array:
        if number == item:
            count += 1
            
    print(item, "has been found in array ", count, " times")
    
    
array = [34, 5, 34, 15634, 5, 76, 34, 55, 5]

item = int(input("Enter a number: "))
count_duplicates("array, item")