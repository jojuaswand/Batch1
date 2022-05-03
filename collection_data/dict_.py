d = {}
print(d, type(d))
d = dict()
print(d, type(d))
d = {"name": "python"}
print(d, type(d))
# d = {key : value}
print(d["name"])
# mutable data cannot be a key but it can be a value
# d = {[1,2]: "name"}
# print(d)
d = {1: 2}
print(d)
d[1] = 3
print(d)
d[7] = 8
print(d)
d[7] = 10
print(d)
# keys cannot have duplicates but values can have duplicates
d = dict(name = "python")
print(d)

