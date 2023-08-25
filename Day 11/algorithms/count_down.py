def count_down(n):
    while n >= 1:
        print(n)
        n -= 1
        
n = int(input('Enter n  :  '))
count_down(n)


# Base case:
def count_down(n):
    if n == 0:
        return # exit function
    print(n)
    count_down(n-1)
    
n = int(input("enter n :  "))
count_down(n)