
#WAP to count number of student with 70 marks in following tuple 
number=(70,80,50,60,70)
print(number.count(70))


# Take tuple input as numbers separated by space
numbers = tuple(map(int, input("Enter student marks separated by space: ").split()))

# Take the mark to count
mark = int(input("Enter the mark to count: "))

# Count how many times the mark appears
print(f"Number of students with {mark} marks:", numbers.count(mark))


""" 📌 Key Takeaways for Interview

split() → mandatory for multiple inputs

map() → needed if you want numbers, not strings

tuple() → optional, list works as well """