#WAP to store following word meanings in python dictionary:
Dict={
    "cat":"a small animal",
    "table": ["a furniture","list of fact"]
}

print(Dict)
#WAP to enter marks of 3 subject from user and store them in dict. start with an empty dict and add one by one. use subject name as key & marks as value.
dict2={}
a=int(input("enter the marks:")) 
dict2.update({"phy":a})
a=int(input("enter the marks:"))
dict2.update({"chem":a})
print(dict2)