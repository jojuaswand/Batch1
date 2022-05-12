
def rev_(x):
    s1 = ""
    for i in x:
        s1 = i + s1

    print(s1)


# rev_("hello")
# rev_("hello world")
# rev_("elephant")

def pr10(value):
    for i in range(10):
        print(value)


# pr10("hi")
# pr10("bye")
# pr10(10)

def eveodd(x):
    if x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')


# eveodd(123)
# eveodd(1224)

def cevod(c):
    if isinstance(c, (str, list, tuple, set)):
        for i in c:
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
    else:
        print(f'{c} is individual type or a dictionary')


# cevod([1, 2, 3, 4])
# cevod(1)

# def add_(a, b):
#     print(a + b)

#
# add_(4, 5)
# add_(4, 5, 6)

def add_(*args, **kwargs):
    print(args, kwargs)
    sum = 0
    for i in args:
        sum += i
    for i in kwargs:
        sum += kwargs[i]
    print(sum)


# add_(4, 5, 6, a=10)
# add_(5, 5, a=10, b=10)
# add_(a=10, 5)SyntaxError: positional argument follows keyword argument


l = ["hello", "hi", "welcome", "elephant"]

def lp(*args, **kwargs):
    l1 = []
    for i in args:
        for j in i:
            if len(j) % 2 == 0:
                l1.append(j[::-1])
            else:
                l1.append(j)

    for i in kwargs:
        for j in kwargs[i]:
            if len(j) % 2 == 0:
                l1.append(j[::-1])
            else:
                l1.append(j)
    return l1


# print(lp(l, l1=["hello", "hi", "bye"]))
# print(lp(l,l,l,l))
# print(lp(l, l, l1=["hello", "hi", "bye"], l2=["hello", "hi", "bye"]))

def disp():
    print("hello")


# disp()

