# Nested if
# somtimes we use if inside another if
# This is call nested if


"""
# example 1
print("-----------------------vote eligibility checker--------------------------")
age = int(input("enter your age:"))
check_citizen = input("are you Nepali Citizen(y/n)")
if age >= 18:
    if check_citizen == "y":
        print("you can vote")
    else:
        print("you are not eligible for voting:( ")
else:
    print("you are not allowed to vote")
"""


# example 2
# program to check whether a given number is postive even number or not

num = int(input("enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Postive even number")
else:
    print("number is negative")
