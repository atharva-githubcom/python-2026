#WAP to take input of movie name from user and append it into lists
movies=[]
movies.append(input("enter the name of movie1:"))
movies.append(input("enter the name of movie2:"))
print(movies)

#WAP to check if list conatins palindrome of element or not 

# Take input as a string
user_input = input("Enter a word or number: ")
# Convert input to list (each character is an element)
lst = list(user_input)
# Check palindrome using slicing
if lst == lst[::-1]:
    print("Palindrome")
else:
    print("NOT Palindrome")

#WAP program for sorting the number.
inpu = list(map(int, input("Enter numbers: ").split()))
inpu.sort()
print("Ascending:", inpu)
inpu.sort(reverse=True)
print("Descending:", inpu)

#WAP program for sorting the charcater

inpu = input("Enter letters separated by space: ").split()
inpu.sort()
print("Ascending:", inpu)
inpu.sort(reverse=True)
print("Descending:", inpu)    
