# s = set()
# print(s, type(s))
# s = {1, 2, 3, 4, 5}
# s1 = set(i for i in s)
# print(s1)
# s2 = set()
# for i in s:
#     s2.add(i)
# print(s2)
# s = set(range(11))
# s1 = set(i for i in s if i % 2 == 0)
# print(s1)
# s = {i * 2 if i % 2 == 0 else i ** 2 for i in range(0, 11)}
# print(s)

# d = {i: i for i in range(11)}
# print(d)

# s = "hello"
# s = ["hello", "hi", "world"]
# s = {"name": "python", "age": 2, "rno": 1}
# d = {i: v for i, v in enumerate(s)}
# d = {i: v for i, v in enumerate(s.values())}
# d = {i: v for i, v in enumerate(s.items())}
# d = {v: k for k, v in s.items()}
# print(d)

# s = "hello this is my world"
# d = {i: len(i) for i in s.split()}
# print(d)

# l = list(range(21))
# d = {}
# for i in l:
#     if i % 2 == 0:
#         if "even" not in d:
#             d["even"] = [i]
#         else:
#             d["even"].append(i)
#     else:
#         if "odd" not in d:
#             d["odd"] = [i]
#         else:
#             d["odd"].append(i)
# print(d)
# l = list(range(21))
# d = {"even": [i] if i % 2 == 0 if "even" not in d else i for i in l}

# s = "hi this is python, python is programming language"
# d = {i: s.count(i) for i in s.split()}
# print(d)