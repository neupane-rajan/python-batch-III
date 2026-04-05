# elif: if we have many condition then we use elif

"""
#syntax:
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
...........
else:
    statement
# else is optional
"""

# grading system
"""
90+ 100-> A+
80-89->A
70-79->B+
60-69->B
50-59->C+
40->49->C
40>-> fail
"""

marks = int(input("Enter your marks in percentages:"))

if marks >= 90 and marks <= 100:
    print("you got A+")
elif marks >= 80 and marks < 90:
    print("you got A")
elif marks >= 70 and marks < 80:
    print("you got B+")
elif marks >= 60 and marks < 70:
    print("you got B")
elif marks >= 50 and marks < 60:
    print("you got C+")
elif marks>=40 and marks<50:
    print("you got C")
elif marks<40:
    print("fail")
else:
    print("Invalid marks")