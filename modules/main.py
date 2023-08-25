from calcul import add
from calcul import minus
from calcul import multi
x = int(input("enter X : "))
y = int(input("enter Y : "))

#result = add(x, y)
#result = minus(x, y)
result = multi(x, y)
print(f"{x} x {y} = {result}")


from calcul import say_hi
say_hi("ahmed")

#----> installing external packages:
#pip install art
# pip3 install art
#python3 -m install art