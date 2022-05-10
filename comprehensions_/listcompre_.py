l = [1, 2, 3, 4, 5]
l1 = []
# for i in l:
#     l1.append(i)
# print(l1)
l1 = [i for i in l]
# print(l1)

# l = list(range(21))
# l1 = []
# for i in l:
#     if i % 2 == 0:
#         l1.append(i)
# print(l1)

l1 = [i for i in range(21) if i % 2 == 0]
# print(l1)


l1 = []
for i in range(21):
    if i % 2 == 0:
        l1.append(i ** 2)
    else:
        l1.append(i)
# print(l1)

l1 = [i**2 if i % 2 == 0 else i for i in range(21)]
# print(l1)

# syntax
# [return value for loop]
# [return value of if |for loop |if statement]
# [return value of if |if statement |else |return value of else |for loop]

# l = ["hi", 1, "hello", 2, "world"]
# l1 = [i for i in l if isinstance(i, str)]
# print(l1)
# l2 = [i if isinstance(i, str) else i**2 for i in l]
# print(l2)
# l3 = [i[::-1] if isinstance(i, str) else i*2 for i in l]
# print(l3)

l = ["hello", "hi", "bye", "good"]
# even = [i for i in l if len(i) % 2 == 0]
# odd = [i for i in l if len(i) % 2 != 0]
# print(even, odd)
# odd = []
# even = [i if len(i) % 2 == 0 else odd.append(i) for i in l]
# print(even, odd)

