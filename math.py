#my fisrt python program
from math import sqrt
print("Enter your name:")
name = str(input())
print(f"Hello {name}")

def sum():
    print("Enter first number:")
    a=int(input())
    print("Enter second number:")
    b=int(input())
    sum = a+b
    sqrt1 = sqrt(sum)
    return print(f"Sum is equal to : ", sum , f"Squareroot is equal to : ", sqrt1)
    

sum()

'''

def squareroot():
    print("Enter number:")
    a=int(input())
    sqrt1 = sqrt(a)
    return print(f"Squareroot is equal to : ", sqrt1)

squareroot()
'''