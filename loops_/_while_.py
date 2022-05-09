# s = "hello"
# s1 = ""
# for i in s:
#     s1 = i + s1
#
# # print(s1)
# s = 'hello'
# s1 = ''
# i = 0
# while i < len(s):
#     s1 = s[i] + s1
#     print(s1)
#     i += 1
#
# print(s1)

# l = []
# for i in range(1, 11):
#     # print(i)
#     l.append(i)
# print(l)

# l = []
# i = 1
# while i <= 10:
#     l.append(i)
#     i += 1
#
# print(l)

# l = []
# i = 10
# while i >= 1:
#     l.append(i)
#     i -= 1
# print(l)

a = 0
b = 1
l = []
while a <= 50:
    l.append(a)
    c = a + b
    a = b
    b = c
    # print(l)
# print(l)

n = 5
a = 0
b = 1
while a <= n:
    if a == n:
        print(f"{n} is fibonacci number")
        break
    c = a + b
    a = b
    b = c
    # print(f"{n} no fibonacci number")



