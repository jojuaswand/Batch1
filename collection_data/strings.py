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
s = "hello \@"
# s = r"hello \@\"
print(s)







