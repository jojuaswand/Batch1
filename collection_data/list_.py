# l = [] #empty list is the default value of list
# print(l, type(l))
# # list has elements and those elements can be of any type
# l = [1, 1.2, 1+2j, "hello"]
# print(l, type(l))
# l = list()
# print(l, type(l))
# l = list("hello")
# print(l)
# l = [1, 2, 3, 4, 5]
# print(l)
# l = [1]
# print(l)
#
# l = [1, 2, 3, 4, 5, 6]
# for i in l:
#     print(i, type(i))
#
# # 0  1  2   3    forward index
# # 1, 2, 3, "hello"
# # -4 -3 -2  -1   backward index
#
# l = [1, 2, 3, "hello"]
# print(l[2])
# print(l[3])
# print(l[3][0])
# print(l[3][0:2])
#
# l.append(4) # append inserts the value at the last for list
# l.insert(0, 5) #insert takes two values index position and value to be inserted
# print(l)
#
# print(l.append)
# print(l.insert)
#
# # print(l.pop()) #pop removes the last element by default from list
# # print(l.pop(0)) #index value can be given inside pop
#
# print(l.remove(3)) #can directly remove the value
# print(l)

# l = [1, 2, 3, 4, 5, 6]
# # l.reverse() # reverses the list and affects original list
# l = [6, 7, 5, 2, 8, 3, 1, 9]
# print(l)
# # l.sort() #sorts the list and affects the original list
# l.sort(reverse=True) #sorts the list in reverse order
# l = ["hello", "no", "bye", "i"]
# l.sort() #based on alphabets
# l.sort(key=len) #based on length
# print(l)
