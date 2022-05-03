# t = 1, 2
# print(t, type(t))
# # comma separated value without boundaries is considered a tuple by python
# t = (3, 4)
# print(t, type(t))
# # tuple has () boundaries
# t = tuple()
# print(t) #empty() is the default value
# t = tuple("hello")
# print(t)
# t = (1)
# print(t, type(t))
# t = (1,)
# print(t, type(t)) #single valued tuple requires a comma after value
#

t = (1, 2, 3, 5, 1, 11, 12, 2, 55, 5)
print(t.index(3))
print(t.count(1))
print(t.count(5))
print(t.count("x"))

