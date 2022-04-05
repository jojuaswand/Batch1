x = 10
simran = 1
y = 20
print(x,y)
"x".isidentifier()
"simran".isidentifier()
"_simran".isidentifier()
"1simran".isidentifier()
" simran".isidentifier()

print(id(x))
print(id(y))
x = 5

print(id(x))
print(id(y))
y = 5
print(id(x))
print(id(y))

id(10)

help("keywords")

import keyword #keyword is a module / library of python
keyword.kwlist
print(keyword.iskeyword("x"))
print(keyword.iskeyword(x))
print(keyword.iskeyword(y))
print(keyword.iskeyword("true"))
print(keyword.iskeyword("True"))

