
#Practice Question 1 (Easy)
#Write a Python function named square() that:
#Takes one number from the user
#Calculates the square of that number
#Prints the result
def square(a):
     print(f"The square of {a} is",a*a)
num=int(input("Enter the number for which you want to calculate the square:"))
square(num)     


#Practice Question 2
#question:
#Write a function named add_numbers() that:
#Takes two numbers from the user
#Returns their sum
#Prints the result outside the function

def add_numbers(a,b):
    sum=a+b
    return sum
a=int(input("enter the frist number:"))
b=int(input("enter the second number:"))
result=add_numbers(a,b)
print(result)

#Write a function check_even_odd() that:
#Takes one number as parameter
#Returns "Even" if the number is even
#Returns "Odd" if the number is odd
#Print the result outside the function
def check_even_odd(a):
    if(a%2==0):
        return "even"
    else:
       return "odd"
a=int(input("enter the number:"))
value=check_even_odd(a)
print(value)


#Practice Question 4 (Comparison Logic)
#question:
#Write a function find_max(a, b) that:
#Takes two numbers
#Returns the greater number
#Print the result outside the function


def find_max(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("enter the number:"))
b=int(input("enter the number:"))
result=find_max(a,b)
print("the number which is great is",result)


#write the code to find the factorial:
def factorial(n):
    fact = 1                 # Initialize factorial
    for i in range(1, n+1):  # Loop from 1 to n (inclusive)
        fact = fact * i      # Multiply step by step
    return fact              # Return final factorial

n = int(input("enter the number which factorial you want to calculate: "))
fac = factorial(n)          # Call function and store result
print("The factorial of number is:", fac)  # Print final result

#Write a function convert_to_inr() that:
def convert_to_inr(a):
    result=a*83
    return result
a=int(input("the of the dollar:"))
ouput=convert_to_inr(a)
print("The value is ",ouput)

def convert_to_inr(dollar,rate):
    result=dollar*rate
    return result
dollar=int(input("enter of the dollar:"))
rate=int(input("enter the rate"))
ouput=convert_to_inr(dollar,rate)
print("The value is ",ouput)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this oTask:

#Write a function that:
#1️⃣ Takes one number n
#2️⃣ Calculates the square of the number
#3️⃣ Returns the result
#4️⃣ Print the result outside the function
def square(a):
    squ=a**2
    return squ
a=int(input("Enter the number for which you want find the square:"))
an=square(a)
print(f"The square of {a} is",an)

#Task:

#Write a function that:
#1️⃣ Takes one number n
#2️⃣ Calculates the factorial of n
#3️⃣ Returns the factorial
#4️⃣ Print the result outside the functio


def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter the number for which you want to calculate the factorial:"))
fact=fac(n)
print(f"The factorial of number {n} is:",fact)


#Task:
#Write a function that:
#1️⃣ Takes three numbers
#2️⃣ Returns the largest number
#3️⃣ Print the result outside the function


def large(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("Enter the frist number:"))
b=int(input("Enter the second number:"))  
c=int(input("Enter the Third number:"))  
lar=large(a,b,c)
print("The larger number is:",lar)

#Write a function that:
#1️⃣ Takes one number n
#2️⃣ Prints all numbers from 1 to n
#3️⃣ No return needed (just print inside function)

def pri(n):
    for i in range(1,n+1):
        print("the numbers are:",i)
n=int(input("enter the numbers:"))
pri(n)

#Task:
#Write a function that:
#1️⃣ Takes one number n
#2️⃣ Prints all even numbers from 1 to n
#3️⃣ No return needed


def even(n):
    for i in range(1,n+1):
        if(i%2==0):
            print("The number which divisble by 2 are:",i)
n=int(input("enter the numbers:"))
tot=even(n)
    