"""
While loop syntax
Before each step of the loop, some_condition is computed. As long as its value is true3 ,
the body of the loop is executed. Once it becomes false, we exit the loop without executing
loop_body.
"""

i = 10

while i < 20 :
    print (i)
    i = i+1

"""
Example 1:
Example: The Fibonacci numbers4 form a sequence of integers defined recursively in the
following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subse-
quent number is the sum of the previous two. The first few elements in this sequence are: 0,
1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
a given integer n.
"""

n = 50
a= 0
b= 1

while a <= n:
    print(a)
    c = a + b
    a = c
    b = a