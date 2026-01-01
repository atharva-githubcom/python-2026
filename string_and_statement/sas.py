#WAP to input user's first name & print its length.
str_1=input("enter the name ")
print(len(str_1))

#WAP to find the occurence of $ in the string.
str_2= " $ is the name  of the American currency."
print(str_2.count("$"))

#WAP concatation of string.
str_3="Atharva"
str_4="Gite"
ouput=str_3+str_4
print(ouput)

print(str_3[1:5])  #silicing function 

#WAP to check if an number entered by user is odd or even.
num=int(input("enter the number:"))
if(num%2==0):
    print("The number you entered",num,"is even")
else:
    print("the number you entered",num,"is odd")

#WAP to find the gratest of the 3 number entered by user

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if (num1>=num2 and num1>=num3):
    print(f"the number {num1} is greater")
elif(num2>=num1 and num2>=num3):
    print(f"the number {num2} is greater")
else:
    print(f"the number {num3} is greater")

#WAP to check if a number is a muliple of 7 or not
number= int(input("enter the number:"))
if(number%7==0):
    print(f"The number entered by user which is {number} is multiple of 7")
else:
    print(f"The number entered by user which is {number} is not multiple of 7")


#WAP to check whether a person is eligible for a driving license.
age = int(input("Enter your age: "))

if age >= 80:
    print("You are overage")
elif age >= 18:
    ll = input("Do you have a learner's license? (yes/no): ").lower()
    if ll == "yes":
        print("Apply for DL")
    else:
        print("Apply for LL first")
else:
    print("You are underage")    