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

#Methods in a Class
#A.instance method
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):  ####
        print("Hello, my name is", self.name) ####

s1 = Student("Atharva")
s1.greet()
#✔ self refers to current object
#✔ Can access instance variables

#B.static method
class Student:
    @staticmethod ####
    def info(): ####
        print("Students belong to college")

Student.info()
#✔ No object data used
#✔ Just logic

#del method
class Student:
    collagename="xyz"
    def __init__(self, name, age):
       
        self.name = name
        self.age = age

s1 = Student("Atharva", 21)
del s1  #### This  is a method use to delete the object
print(s1.name)
print(s1.age)
print(s1.collagename)

#private attribute
class Student:
    collagename="xyz"
    def __init__(self, name, age):
       
        self.name = name
        self.__age = age #private attribute this connot access outside the class.

s1 = Student("Atharva", 21)
print(s1.name)
print(s1.age)
print(s1.collagename)

#How to access the private class attribute.
class Student:
    collagename="xyz"
    def __init__(self, name, age):
       
        self.name = name
        self.__age = age ## This is private class attribute.

    def getage(self): # This is function created to access the private class attribute.
        return(self.__age)

s1 = Student("Atharva", 21)
print(s1.name)
print(s1.getage()) # This is way to call private attribute function.
print(s1.collagename)

#inheritance code using the static method
# Parent class
class Car:
    @staticmethod
    def start():
        print("Car starts")
                                ####The the static method is used here becuse it will not call any object 
    @staticmethod
    def stop():
        print("Car stops")


# Child class
class BMW(Car):
    def music_system(self):
        print("BMW has premium music system")


# Object of child class
b = BMW()

Car.start()          # inherited from Car
Car.stop()           # inherited from Car
b.music_system()   # BMW's own method

#single inheritance example

class Parent:
    def show(self):
        print("This is parent")

class Child(Parent):
    def display(self):
        print("This is child")
        
c=Child()   
c.show()         # calls Parent's method
c.display()

#mutlilevel inheritance

class Grandparent:
    def house(self):
        print("Grandparent has a house")

class Parent(Grandparent):
    def car(self):
        print("Parent has a car")

class Child(Parent):
    def bike(self):
        print("Child has a bike")
        
b=Child()   ## Why child object is called ? Because it has access to parent class and grandparent class     
b.house()
b.car()
b.bike()

#Muliple inheritance
class Father:
    def house(self):
        print("House from father")

class Mother:
    def gold(self):
        print("Gold from mother")

class Child(Father, Mother): # Here the child class called the properties of both parent class there is no grandparent class here.
    def bike(self):
        print("Child has a bike")
        
c = Child()  

c.house()   # from Father
c.gold()    # from Mother
c.bike()    # from Child 

#Diferrence between muliple and multilevel 
##In multilevel inheritance, properties are passed level by level from grandparent to parent and then to child.
##In multiple inheritance, a child class inherits from two parent classes and can access properties of both.

#Class method 

class Student:
    college = "XYZ College"   # class variable

    def __init__(self, name, age):### This method  data is different for all for all student
        self.name = name      # instance variable
        self.age = age

    @classmethod ### This method  data is ame for all student
    def show_college(cls):
        print("College:", cls.college)


# Create object
s1 = Student("Atharva", 21)

# Instance variables
print("Name:", s1.name)
print("Age:", s1.age)

# Class method
Student.show_college()

#methods code including 3 methods together 
class Calculator:

    factor = 10   # class variable

    # Instance method
    def add(self, a, b):
        return a + b

    # Static method
    @staticmethod
    def subtract(a, b):
        return a - b

    # Class method
    @classmethod
    def multiply(cls, a):
        return a * cls.factor


# Create object
c = Calculator()

# Instance method (uses object)
print("Addition:", c.add(10, 5))        # 15

# Static method (no object/class data)
print("Subtraction:", Calculator.subtract(10, 5))  # 5

# Class method (uses class data)
print("Multiplication:", Calculator.multiply(5))   # 50

#class method can also called by using the object.
print("multiplication:",c.multiply(10)) 

#Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

Dog().sound()
Cat().sound()

#code using absraction and encapsulation 
class Palindrome:
    def __init__(self,ina):
        self.ina=ina
        
    def check(self):
        if(self.ina==self.ina[::-1]):
            return "palindrome"
        else:
            return "NO"
c=Palindrome(ina=input("enter the word:"))
print(c.check())