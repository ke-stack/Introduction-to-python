"""
Example 1
We are given some positive integer n. Let’s compute the factorial of n and assign
it to the variable factorial. The factorial of n is n! = 1 · 2 · . . . · n. We can obtain it by
starting with 1 and multiplying it by all the integers from 1 to n.

"""


factorial = 1
n = 4


for i in range(1, n+1 ):
    factorial *= i
    print(factorial)

"""
Example 2
Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
should consist of n rows, where n is a given positive integer, and consecutive rows should
contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:
*
* *
* * *
* * * *
"""

for i in range(1, n+1):
        print(('*'+ ' ') * (i))
    

"""
Example 3
Create a function that takes in the height of a triangle as an argument and use (*) to draw a isosceles triangle 

"""

def print_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

triangle_height = int(input("Enter the height of the triangle: "))
print_triangle(triangle_height)



print(f'n: {n}')

"""
Example 4
Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
spaces. For example, for n = 4 the triangle should appear as follows
"""

for i in range(n, 0, -1):
     spaces = ' ' * (n - i)
     stars = '*' * (2 * i - 1)
     print(spaces + stars)