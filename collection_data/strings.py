# print("hello")
# print(type("hello")) #string is collection of characters

s = "hello"  #single line strings
s1 = 'hello' #single line strings
s2 = """ hello  
    bye
    b"""    #multiple line strings
s3 = ''' hello 
    bye 
    b''' #multiple line strings
# print(type(s1), type(s2), type(s3))
# print(s1, s2, s3)
# s4 = str(13235456) #converting in to string
s4 = str() #default value of string is "", '' or empty string
# print(s4)
# print(type(s4))

s = ""
# print(s)
# print(type(s))

s = "123abc!@#"  #characters are kept inside boundaries, "", '' , """, '''
# print(s)

# s = ""hello""  #cannot use boundaries inside
s = '"hello"'
s = "'hello'"
s = '"""hello"""'
s = "'''hello'''"
# print(s)

#raw string
s = "tha\nk you"
s = r"tha\nk you" #whenever there is r or R before string it is considered as raw string
s = "\tha\nk you \t"
s = r"\tha\nk you \t" #to get escape characters without performing its function
# print(s)

s ="\\"
s = r"\\"
# s = "\" SyntaxError: EOL while scanning string literal
# s = r"\"  SyntaxError: EOL while scanning string literal
#strings and raw strings cannot have odd number of backslashes
#backslashes should have a literal after it
# s = "hello \@"
# # s = r"hello \@\"
# print(s)
#
# s = "hello"
# print(id(s))
# print(len(s)) #we will be getting length of sring, counting the number of characters
#
# #index
# s = "hello"
# print(len(s)-1) #max value of index will be length of string -1
# # length: 1,2,3,4,5  index: 0,1,2,3,4
# print(s[0])
# print(s[-1])
# #forward index : 0,1,2,3,4
# #backward index: -length : -1,-2,-3,-4,-5
#
#memory alloctaion
# s = 'hello'
# print(id(s))
# print(id(s[0]))
# print(id(s[1]))
# print(id(s[2]))
# print(id(s[3]))
# print(id(s[4]))

#slicing
# s = "hello world"
# print(s[0], s[1], s[2], s[3], s[4])
# print(s[0:4]) #it will take indexes to slice a string, it will start from a index and end until the given index
# print(s[0:5]) #start index should be same and end index will be required index +1
# print(s[:5]) #start from beginning
# print(s[6:]) #end at the last
# print(s[6:-1])
# print(s[:])
# print(s[-1:-6:1]) #step value by default it will be 1 whuch represents going forward
# print(s[-1:-6:-1])
# print(s[-5:])

#upper & lower()
# s = "A ball BLue"
# print(s)
# print(s.upper()) #converting lower case to uppercase
# print(s.lower()) #converting upper case to lowercase
# a = s.upper() #it will be creating duplicate string
# print(a)
# print(s) #wont affect original string

#count()
# s = "132141516"
# print(s.count("1")) #counting the occurance of the value inside the base value
# print(s.count("5"))
# print(s.count("10")) #it will not throw errors if value doesnt exist it will give us 0
# print(s.count("15"))
# s = 'hello world'
# print(s.count("l"))
# print(s.count("hello"))

#index()
# s = "hello"
# print(s.index("l")) #it will give the index value of the 1st occurance
# print(s.index("i")) #ValueError: substring not found if the value doesnt exist
s = "1a2b3c4d3c1a2b3c"
# print(s.index("3"))
# print(s.index("3", 5)) #second occurance using slice
# print(s.index("3", 9,)) #third occurance
# print(s.index("3",15)) #there is no 4th occurance so throws error
# rindex()
s = "1a2b3c4d3c1a2b3c"
# print(s.rindex("3")) #last occurance nut it checks from the last index mentioned till the start index mentioned
# print(s.rindex("3",13)) #starts from index 13 but checks from the last
# print(s.rindex("3",0,13)) #second occurance using slice
# print(s.rindex("10")) #error if string is not there

# #find()
# s = "1a2b3c4d3c1a2b3c"
# print(s.find("3")) #same as index()
# print(s.find("10")) #instead of error we will get -1 if value doesnt exist
# #rfind()
# print(s.rfind("3")) #same as rindex()
# print(s.rfind("10")) ##instead of error we will get -1 if value doesnt exist



