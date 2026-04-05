# we can use  logical operators with if
# and
# or
# not

# example of and
# write a program to check whether a user is eligible for vote or not

age = 17
nepali_citizen = True

if age >= 18 and nepali_citizen == True:
    pass
    print("Eligible to vote")
# here both condtion must be true to executie if block


# example of or
# if day is saturday or sunday then print weekend
day = "sundey"
if day == "saturday" or day == "sunday":
    print("today is your weekend")

# if not True-> False
# if not False -> True
is_rule_break = False
if not is_rule_break:
    print("you are allowed to go as you have not fine")
else:
    print("please pay your fine otherwise you will be in trouble")


# common mistake while writing
"""
# 1.
incorrect: if age>=18 #missing colon
correct  : "if age>=18:"
 

#2. wrong indentation
if age>=19:
print("adult")

correct:
if age >=18:
    print("Adult")

#3. if age=18 #wrong syntax
correct:
if age==18:
"""
