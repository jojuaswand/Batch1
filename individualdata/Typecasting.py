a = int()
b = float()
c = complex()
d = bool()

# print(a, b, c, d)
a = int(1.4) #convertig float value into int value
# print(type(1.4))
# a = int(1 + 2j) #TypeError: can't convert complex to int because complex is having imaginary value
# a = int(True) #converting boolean value to int value
# print(a)
# print(type(a))

b = float(5) #converting int value to float
# b = float(1 + 2j) #TypeError: can't convert complex to float because complex have imaginary value
# b = float(False) #converting bool value to float value
# print(b)
# print(type(b))

c = complex(1)
c = complex(1,2) #converting int value to complex value
c = complex(1.2)
c = complex(1.2, 2.1) #converting float to complex
c = complex(False, True) #converting bool to complex
# print(c)
# print(type(c))

d = bool(1) #converting int into bool
d = bool(1.1) #converting float to bool
d = bool(1+2j) #converting complex to bool
d = bool(0)
d = bool(0.0)
d = bool(0j) #bool is not actually converting but it is checking if value exist
# print(d)
# print(type(d))




