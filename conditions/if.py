a = 10
b = 11
# print(a == b) #it returns false because a is not same as b
# print(a != b) #it returns true because a is not same as b
# print(a > b)  #it returns false because a is not greater than b
# print(a < b) #it returns true because a is less than b
# print(a >= b) #it returns false because a is not greater or equal to b
# print(a <= b) #it returns true because a is lesser than b even though a is not equal to b

# print(a == b)
# print(a + b)
# if a == b: #if is checking whether the condition is true or not, if condition is true it enters codeblock
#     print(a + b) #this code block is called true block
#
# #if condition is false it doesnt enter the true block and it exits if code block
#
# if a == b:
#     print(a + b)
# else: #it creates a false block
#     print("condition is false")

# a = 11
# b = 12
# if a == b:
#     print(a, b)
# # else a == b: #else cannot take any conditions
# elif a != b: #false block created with a conditional statement
#     print(a)
# else:
#     print("none")
#
# a = "hi"
# b = "bye"
# a = "hello"
# b = "good"
# if len(a) %2 == 0:
#     print(b, 'EVEN')
# elif len(b) %2 == 1:
#     print(a, "odd")
# else: #default false block
#     print("both false")


a = 1
b = 2
a = 2
b = 3
# if a != b:
#     if a %2 == 1: #nested if is a if block inside another if block
#         print(a, "odd")
#     else:
#         print(a, "even")
# else:
#     print("a==b")
# a = 3
# b = 4
# a = "3"
# a = "6"
# if int(a) != b:
#     if int(a) %2 == 1: #nested if is a if block inside another if block
#         print(a, "odd")
#     elif isinstance(a, int):
#         print(a, "even")
#     else:
#         print("inner conditions false")
# else:
#     print("a==b")

# 1 if length of string is even then reverse it else print not even
# s = "mom"
# s = "good"
# s = 'hello'
# if len(s) %2 == 0:
#     print(s[::-1])
# elif isinstance(s, str):
#     print(s, len(s))
# else:
#     print("not even")

#check whether the given number is even or odd
n = 1
n = 2
n = 3
if n %2 == 0:
    print("even")
else:
    print("odd")

s = "hello"
if s.split():
    print("spliting" , s.split("l"))
else:
    print("not spliting")
