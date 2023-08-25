def sum(n):
    s = 0
    for i in range(1, n+1):
        s += 1
    return s 

n = int(input("Enter a number n: "))
result = sum(n)
print(result)
 
 # ctrl + k + c --> turn selected text into comment
 # ctrl + k + u --> turn selected comments into text

def sum(n):
    #Base case:
    if n == 1:
        return 1
    print(n)
    s = n + sum(n-1)
    
    
n = int(input("Enter a number n : ")) 
result = sum(n)
print(result)   