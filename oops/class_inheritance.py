# print(dir(int)) # dir is a inbuilt function which displays all methods functions sub classes variables inside a class, attributes of a class or properties of a object
# class A:
#     no = 10 # this is  a class variable u hvae to use self before it to access
#     def __init__(self, name): # __init__ is a magic method which constructs dictionary values for instances
#         self.name = name
# # self catches instances here it is a and b
#     def display_(self):
#         return f"hello im {self.name} and im {self.no}"
#
# # print(A)
# # print(type(A)) # type is main class or meta class and under that we will be having all the other classes
# # print(A.display_(A))
# a = A("aswand") # a is an instance created by passing class
# print(a.display_())
# print(a.__dict__) #__dict__ is returning a dictionary of instance values created by __int__
# b = A("simran") # b is a n instance created by passing class
# print(b.display_())
# print(b.__dict__, a.__dict__)

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"im {self.name} and im {self.age} years old"

#single level inheritance
class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)

    def disp(self):
        return f"im an child who inherited from parent"
#multilevel inheritance
class C(B):
    def disp(self):
        return super().disp()
# multiple inheritance
class D(B, A):
    def disp(self):
        return super().disp()
    def display(self):
        return super().display()
#hierarchical inheritance
class E(A):
    def __init__(self, name, age):
        super().__init__(name, age)

    def disp(self):
        return f"im an child who inherited from parent"
#hybrid inheritance  in a program if we do more than on etype of inheritance it is called as hybrid
# child = B("aswand", 25)
# print(child.age, child.name, child.__dict__)
# print(child.display())
# child2 = C("ho", 2)
# print(child2.disp())
# child3 = D("hi", 1)
# print(child3.disp(), child3.display())
# child4 = E("nd", 4)
# print(child4.display())

class En:
    a = 10 # public
    _a = 20 # protected
    __a = 30 # private
    def disp(self):
        return f"{self.a}, {self._a}, {self.__a}"

print(En.a)
print(En._a)
# print(En.__a)
print(dir(En))
print(En._En__a)
print(En.disp(En))

# encapsulation means storing the values in a space
# abstraction getting functionalities without knowing values
