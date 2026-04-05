# typecasting  : type casting means changing one data type into another data type.

# string,float,boolen to integer : for converting string into integer we can use int()
# only whole number string can be converted into intger if we give another data types then it will show use Error(ValueError)
num1 = "10"
num2 = "20"
float_num = 1.5
int_num1 = int(num1)
int_num2 = int(num2)
sum = int_num1 + int_num2
ismale = True  # if we convert boolean into integer then it will show 1 for true and 0 for false

# print(sum)


# print(float_sum)

# integer,boolean, string to float : using float() we can also change Integer into Float
weight1 = "79"
float_weight1 = float(weight1)
num = 12
float_num = float(num)
boolean = False
float_boolean = float(boolean) # if we convert booelan into float then it will show 1.0 for true and 0.0 for false
# print(type(float_num))

# any data types to string : for converting any data types into string we can use str() function
x = 1
y = 1.1
z = True
none = None
list1 = [1, 2, 3, 4, 5, 6, 7]
dict1 = {
    "name": "ram",
}
set1 = {1, 2, 3, 4, 5, 6}
tuple1 = (1, 2, 3, 4, 5)
x1 = str(x)
y1 = str(y)
# print(type(x1))
# print(type(y1))
