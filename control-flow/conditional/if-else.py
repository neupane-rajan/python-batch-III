"""
syntax:
if condition:
    statement
else condition:
    statemetn
"""


# write a program that tell whether you are eligible to vote or not
# if  if condtion is false then only else condtion will execute
age = int(input("enter your age: "))
if age>=18:
    print("you can vote")
else:
    print("you cannot vote")


# take a marks from user if marks is greater than or equal to 40 then print you passed else print you failed