# While loop: 
# a while loop is used when you want to repeat something until a condition becomes false.

# syntax:
"""
while condition:
    # code or statement
"""

# x =1
# while x<=5:
#     print(x)
#     x +=1 #x = x+1

x=1
while True:
    print(x)
    x = x+1
    if x >5:
        break

"""

# infinite loop
x=1
while False:
    print(x) 
    x = x+1
 
# this is also infinite loop
x = 1
while x <= 5:
    print(x)

"""