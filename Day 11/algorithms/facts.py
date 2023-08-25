result = 1
n = int(input('Enter the number N: '))

#using for loop
for i in range(1, n+1):
    result = result * i
    
print(n, "! = ", result)


# using while loop 
counter = 1
result = 1
n = int(input('Enter the number N: '))

while counter <= n:
    result = result * counter
    counter += 1
    
print(result)


# recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input('Enter the number N: '))
result = factorial(n)
print(result)