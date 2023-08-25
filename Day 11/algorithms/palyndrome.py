def check_palyndrome(i):
    reverse = i[::-1]
    if (i == reverse):
        return True
    return False



x = input(("entrer une valeur : "))
if (check_palyndrome(x)):
    print("palyndrome!")
else:
    print("not palyndrome!")
    
def check_palyndrome(word):
    n = len(word)
    is_palyndrome = True
    
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            is_palyndrome = False
            
    if is_palyndrome:
        print(word, "is palyndrome!")
    else:
        print(word, "is not palyndrome!")
        
word = input("Enter a word:  ")
check_palyndrome(word)