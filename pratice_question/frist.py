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


