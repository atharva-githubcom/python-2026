#🟢 Practice Question – 1 (List + User Input)

#Write a program to take multiple numbers from the user in one line, store them in a list, and display the list.

li=list(map(int,input("enter the number:").split()))
print(li)
#list → map → int → input → split

#🟢 Practice Question – 2
#Write a program to:

#Take input from the user (it can be number or word)
#Store the input in a list
#Check whether the input is a palindrome
#Condition: You must use list slicing to check palindrome

inp=list(input("enter the number and word:"))
if(inp==inp[::-1]):
    print("plaindrome")
else:
    print("no ")
    
    
#🟢 Practice Question – 3    
#Write a program to:
#Take student marks from the user in one line
#Store them in a tuple
#Ask the user for a specific mark
#Count how many students got that mark

mo = tuple(map(int, input("Enter the marks of the student: ").split()))
re = int(input("Enter the mark you want to count: "))
count = mo.count(re)
print(f"Total count of students having marks {re} is: {count}")


#🟢 Practice Question – 4 (Dictionary – Store Subject Marks)
#Write a program to:
#Take marks of Physics, Chemistry, and Maths from the user
#Store them in a dictionary with subjects as keys
#Print the dictionary

dict={}
a=int(input("enter the marks:"))
dict.update({"phy":a})
a=int(input("enter the marks:"))
dict.update({"chem":a})
a=int(input("enter the marks:"))
dict.update({"maths":a})
print(dict)

#🟢 Practice Question – 5 (Set – Remove Duplicates)
#Write a program to:
#Take multiple numbers from the user in one line
#Store them in a set
#Print the set to show only unique values

sets=set(map(int,input("enter the numbers:").split()))
print(sets)

# Write Python 3 code in this online editor and run it
i=1
even_count=0
od_count=0
while(i<=20):
    if(i%2==0):
        print(i,even_count,"even")
        even_count +=1
    else:
        print(i,od_count,"the number is odd")
        od_count +=1
    i +=1
print("the total count is ",even_count)    
print("the total  count of odd is ",od_count) 


#Print numbers from 1 to 20, but:
#If the number is divisible by 4, print "Quad"
#If the number is divisible by 6, print "Hex"
#If the number is divisible by both 4 and 6, print "QuadHex"
#Otherwise, print the number

for i in range(21):
    if(i%4==0 and i%6==0):
        print (i,"QuadHex")
    elif(i%4==0):
        print(i,"quad");
    elif(i%6==0):
        print(i,"hex")
    else:
        print(i)
        
        
#Task:
#Print numbers from 1 to 10
#Rules:
#If number is divisible by 3 → print "Three"
#Otherwise → print the number 

for i in range(1,11):
    if(i%3==0):
        print(i,"three")
    else:
        print(i)
        
        
#Task:
#Print numbers from 1 to 15
#Rules:
#If number is divisible by 3 and 5 → print "ThreeFive"
#Else if divisible by 3 → print "Three"
#Else if divisible by 5 → print "Five"
#Else → print the number 
for i in range(1,16):
    if(i%3==0 and i%5==0):
        print(i,"Threefive")
    elif(i%3==0):
        print(i,"three")
    elif(i%5==0):
        print(i,"five")
    else:
        print(f"this is the number:{i}")
        
#Task:
#Print numbers from 1 to 30
#Rules:
#If number is divisible by 2 and 3 → print "TwoThree"
#Else if divisible by 2 → print "Two"
#Else if divisible by 3 → print "Three"
#Else → print the number 

for i in range(1,31):
    if (i%6==0):
        print("twothree")
    elif(i%2==0):
        print("two")
    elif(i%3==0):
        print("three")
    else:
        print(i)


#write the code to find the factorial:
def factorial(n):
    fact = 1                 # Initialize factorial
    for i in range(1, n+1):  # Loop from 1 to n (inclusive)
        fact = fact * i      # Multiply step by step
    return fact              # Return final factorial

n = int(input("enter the number which factorial you want to calculate: "))
fac = factorial(n)          # Call function and store result
print("The factorial of number is:", fac)  # Print final result        


