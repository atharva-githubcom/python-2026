#way 1to write code using with
with open("demo.txt", "a+") as f:
    a = f.write("\n" + input("Enter the string: "))
   

#way 2 to write the code    
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()