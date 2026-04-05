# for loop is used when we know how many times to repeate

# syntax:
"""
for variable in sequence:
    #code or statement

# for -> for vaneko for-loop define garne keyword ho
#variable-> jasma temporary value store garna sakinxa
# sequence -> sequence vaneko chai collection , example ko lagi (list , range, string, set... etc)


# example
# in below example loop start from 1 and end at 6 but 6 is not included in the loop

# range
# range is used to generate a sequence of numbers.
# range(x)-> it by default start from 0 and end at x but single value is not included in the loop
# range(x, y) -> it start from x and end at y but y is not included in the loop
# range(x, y, z) -> it start from x and end at y but end is not included in the loop and z is used to specify the increment value(how much step we want to take)
# range(x, y, -z) -> it start from x and end at y but end is not included in the loop and -z is used to specify the decrement value(how much step we want to take)
for i in range(6):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)
"""

for i in range(10,0,-1):
    print(i)