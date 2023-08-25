# for loop 
#--> number of reps is known

names = ["yassin", "mortadha", "touquaa"]

print("\nUsing range function\n")
for i in range(1, len(names)):
    print(names[i])

print("\nUsing list iteration\n")
for name in names:
    print(name)

# while loop
#--> number of reps is unknown
#--> stop condition
counter = 0

while counter < 100:
    print(counter)
    counter += 1 

# exercice : while loop that stops on negative number

counter2 = 20
while counter2 > -1:
    print(counter2)
    counter2 -= 1