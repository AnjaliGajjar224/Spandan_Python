# print("Hello World",end=' ')
# print('Hello World')

# print("Hello World",end='\t')
# print('Hello World')

# print("Hello World",end='text')
# print('Hello World')

# print("Hello World",end='\n')
# print('Hello World')

# print("Hello World",end='')
# print('Hello World')

# """
# Escaping Characters

# \n  --> New Line
# \t  --> Tab
# \r  --> Carriage Return
# \b  --> Backspace
# \
# """
# print("Good M\borning")
# print("Python is a programming language\rJava")

# print("Alpha Said:'Good Morning'")

# print('Alpha Said:"Good Morning"')

# """
# Hello\namaste\thank you\bye
# """
# print("Hello\ \bnamaste\ \bthank you\ \bbye")
# print("Hello\\namaste\\thank you\\bye")

# print("Alpha said:\"Good Morning\"")

"""
Numeric Data Types
Integers
Floats
Complex Numbers

Sequence Data Types
Strings
Tuples
Lists

Boolean

Set

Dictionary
"""
"""
Arithmetic Operators
+ , - , * , / , % , ** , //

Comparison Operators
== , != , > , < , >= , <=

Assignment Operators
= , += , -= , *= , /= , %= , **= , //=

Bitwise Operators
& , | , ^ , << , >>

Logical Operators
and , or , not

Membership Operators
in , not in

Identity Operators
is , is not
# """
# a = 10

# a = ++a

# print(a)

# print(print(print("Hello")))

# if True:
#     print("True")

# i = 2,3
# j = 4,5

# add = i + j
# print(add)

# for i in range(1,10):
#     print(i)
#     if i == 3:
#         break

# for i in range(1,10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     pass

# a = 10
# print(type(a))             # <class 'int'>

# b = 10.0
# print(type(b))             # <class 'float'>

# c = 10 + 10j              
# print(type(c))             # <class 'complex'>

# num1 = int(input("Enter a number: "))

# num2  = float(input("Enter a number: "))

# num3 = complex(input("Enter a number: "))

# print(num1)
# print(num2)
# print(num3)

"""
1) Take 5 float Numbers from the user and find sum and average of that numbers.
"""

"""
Conditionals Statements

1) if condition:
    code

2) if condition1:
    code1
   elif condition2:
    code2
    .
    .
    .
    else:
     code3

3) if condition:
    code
   else:
    code
"""

# num1 = 25
# num2 = 10

# if num1 > num2:
#     print("num1 is greater than num2")
# else:
#     print("num2 is greater than num1")

# print("num1 is greater than num2") if num1 > num2 else print("num2 is greater than num1")

"""
1.  A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

2. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

3. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

4. A student is given marks in 5 subjects. If marks are greater than 150 then he/she will be allowed to sit in exam. Otherwise he/she will not be allowed to sit in exam.
"""

# num1 = 15
# num2 = 2

# print("Division : ",num1/num2)               # 15 / 2 = 7.5
# print("Floor Division : ",num1//num2)        # 15 // 2 = 7
# print("Remainder: ",num1%num2)              # 15 % 2 = 1
# print("Exponent: ",num1**num2)              # 15 ** 2 = 225

# def lcm(a,b):

#     # Choose the greater number
#     if a > b:
#         greater = a
#     else:
#         greater = b

#     while(True):
#         if((greater % a == 0) and (greater % b == 0)):
#             lcm = greater
#             break
#         greater += 1

#     return lcm

# # print("LCM of two numbers is : ",lcm(6,4))

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# print(f"LCM of two numbers {num1} and {num2} is {lcm(num1,num2)}")

"""
Task:
------------
Take full name from the user :

Input:

Full name: John Michael Smith

Output:

J.M.Smith
"""

name = input("Enter your full name(firstname+middlename+lastname): ")

part1 = name[0]
part2 = name[name.index(" ")+1]
part3 = name[name.rindex(" ")+1:]

print(part1+"."+part2+"."+part3)

"""
Task 2:
------------
Take a string from the user and find the total number of vowels, consonenets and white spaces in the string.

e.g.

    Input:
    Python Programming

    Output:
    Vowels: 4
    white spaces: 1
    consonets : 13

"""

