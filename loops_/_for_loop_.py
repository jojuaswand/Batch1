# for is a keyword which helps us to assign
# a value to a variable for iteration
# for defines a syntax
# for will be having a code block

# s = "hello"
# for i in s:
    # print(i)

# for i in range(len(s)):
#     print(s[i])

# for i in range(len(s)):
#     print(i, s[i])

# s = "hello"
# s1 = ""
# for i in s:
#     s1 = s1 + i
#     print(s1)
# print(s)
# print(s1)

# for i in range(10):
#     if i %2 == 0:
#         print(i, "even")
#     else:
#         print(i, "odd")
#

# for i in range(1, 11):
#     if i %2 == 0:
#         print(i, "even")
#     else:
#         print(i, "odd")

# for i in range(1, 11, 2):
#     print(i)

# for i in range(0, 11, 3):
#     print(i)

# s = "hello"
# # s1 = s[::-1]
# s1 = ""
# for i in s:
#     s1 = i + s1
#     print(s1)
# # print(s1)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# for i in l:
#     print(i)
# for i in s:
#     print(i)

# for i in l:
#     if i % 2 == 0:
#         print(i)
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# for i in s:
#     if i % 2 == 0:
#         print(i)
#
# print(list(range(10)))
# print(set(range(11)))
# l = list(range(21))
# evenl = []
# oddl = []
# for i in l:
#     if i % 2 == 0:
#         evenl.append(i)
#     else:
#         oddl.append(i)
#
# print(evenl, oddl)

# evens = set()
# odds = set()
# for i in range(21):
#     if i % 2 == 0:
#         evens.add(i)
#     else:
#         odds.add(i)
#
#
# print(evens, odds)


# l = ["hi", "bye", "hello", "good"]
# l1 = []
# for i in l:
#     if len(i) % 2 != 0:
#         l1.append(i[::-1])
#     else:
#         l1.append(i)
#
# print(l1)

# s = {"hi", "bye", "hello", "good"}
# s1 = set()
# for i in s:
#     if len(i) % 2 == 0:
#         s1.add(i)
#     else:
#         s1.add(i[::-1])
#
# print(s1)



# l = ["hi", "bye", "hello", "good", "apple"]
# l1 = []
# for i in l:
#     if i[0] in "aeiouAEIOU":
#         l1.append(i)
#
# print(l1)



# s = {"hi", "bye", "hello", "good", "apple"}
# s1 = set()
# for i in s:
#     if i[0] not in "aeiouAEIOU":
#         s1.add(i)
#
#
# print(s1)

d = {"name": "python", "age": 2, "rno": 1}
# for i in d:
#     print(i)

# for i in d:
#     print(d[i])

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

d = {"name": "python", "age": 2, "rno": 1, 1: 2}

# for i in d:
#     if isinstance(i, str):
#         print("key is string")
#     else:
#         print("not a string")


# d = {"name": "python", "age": 2, "rno": 1, 1: 2}
# d1 = {}
# d2 = {}
# for i in d:
#     if isinstance(i, str):
#         d1[i] = d[i]
#     else:
#         d2[i] = d[i]
# print(d1)
# print(d2)

# d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
# even = {}
# odd = {}
# for i in d:
#     if d[i] % 2 == 0:
#         even[i] = d[i]
#     else:
#         odd[i] = d[i]
#
# print(even)
# print(odd)

# s = "hello world"
# d = {}
# for i in range(len(s)):
#     if s[i] in "aeiouAEIOU":
#         d[i] = s[i]
#
# print(d)

# d = {"name": "python", "age": 2, "rno": 1, 1: 2}
# d1 = {}
# for i, v in enumerate(d):
#     d1[i] = v

# for i, v in enumerate(d.items()):
#     d1[i] = v
#
# print(d1)

# print(list(enumerate(d)))
# print(list(enumerate(d.values())))
# print(list(enumerate(d.items())))
