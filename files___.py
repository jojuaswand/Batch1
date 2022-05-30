path = r"C:\Users\jojua\PycharmProjects\batch1\file1.txt"
# file = open(path) # opening a file
# print(file.read()) # reading a file
# file.close()
# print(file.read()) ValueError: I/O operation on closed file.

# file = open(path)
# print(file.readline()) reading a single line
# print(file.readline()) next line
# print(file.readline())
# print(file.readline())

# file = open(path)
# print(file.readlines()) reading all the lines as strings inside a list

# file = open(path, "r") # r represents read mode and by default it was read mode
# print(file.write("hi")) io.UnsupportedOperation: not writable because opened in read mode
# with open(path, "r") as file:
#     print(file.read())
#     # a = file.read() #storing file data as string
#     # a = file.readlines() # storing file data as list
#     # print(len(a))
#     print(file.tell()) # checking cursor position
#     file.seek(0) # sets the cursor position to required position
#     print(file.tell())
#     print(file.readline())

# with open(path, "w") as file_:
#     print(file_.write("python\n"))
#     print(file_.writelines(["sandeep, akash , shakthivelu, surya \n",
# "yaseen, akhil, atchaya, abhishek, vignesh \n", "manikandan, prasana, madhubalan, raj kumar, abidhesh \n"
# , "harshitha, aswand, virat kohli, vikash \n",
# "rohith sharma, dhoni, vijay, saranya \n",
# "anushka sharma, nayanthara, vijay sethupathy, samantha\n"
# ,"raghavendra, elahee\n"]))

# with open(path,"a") as file_:
#     print(file_.write("hello\n"))
#     print(file_.writelines("hello"))

# with open("newfile.txt", "a") as file_:
#     print(file_.write("hello"))
# write and append mode creates a file if file not existing

# with open("newfile1.txt", "x+") as cfile:
#     print(cfile.read())
#     print(cfile.write("hello"))
# + after any mode will allow us to perform multiple modes apart from the mentioned mode


pathj = r"C:\Users\jojua\PycharmProjects\batch1\file2.JSON"
import json
# d = {"name": "somename", "age": 50, "place": "las vegas"}
# print(d, type(d))
# c = json.dumps(d)
# print(c, type(c))
# f = json.loads(c)
# print(f, type(f))

d = {"name": "somename", "age": 50, "place": "las vegas"}

# with open(pathj, "r+") as jfile:
#     json.dump(d, jfile)

# with open(pathj, "r+") as jfile:
#     print(json.load(jfile))
pathp = r"C:\Users\jojua\PycharmProjects\batch1\file3.pkl"
import pickle

# a = "hello"
# a = 10
# print(a, type(a))
# b = pickle.dumps(a)
# print(b, type(b))
# c = pickle.loads(b)
# print(c, type(c))
# a = "hello"
# pathp = r"C:\Users\jojua\PycharmProjects\batch1\file3.pkl"
# with open(pathp, "wb") as pfile:
#     pickle.dump(a, pfile)
#
# with open(pathp, "rb") as pfile:
#     print(pickle.load(pfile))
#





