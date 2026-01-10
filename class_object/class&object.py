#paramitarized constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Atharva", 21)
print(s1.name)
print(s1.age)

#deafult constructor
class Student:
    def __init__(self):
        self.name = "Atharva"
        self.age = 21

s1 = Student()
print(s1.name)
print(s1.age)

#classvariable and object variable
class Student:
    collagename="xyz"  #classvariable
    def __init__(self, name, age):
       
        self.name = name    #object variable
        self.age = age      #object variable

s1 = Student("Atharva", 21)
print(s1.name)
print(s1.age)
print(s1.collagename)
