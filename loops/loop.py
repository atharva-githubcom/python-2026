#WAP to print number from 1 to 100 using for 
for i in range(100):
    print("number",i)

#using while 
i=1  
while i<=100:
    print("numbers:",i)   
    i += 1 


#WAP to print number from 100 to 1 using for   
for i in range(100, 0, -1):
    print(i) 
#using while    
i=100
while i>=1:
    print("numbers:",i)
    i -=1



#Print numbers from 1 to 10 and count how many even numbers are there.  
i=1
count=0
while(i<=10):
    if(i%2==0):
        print(count,i,"even")
        count +=1
    i +=1
print("totall number of even number are:", count)    
  
count +=1
        
i = 1
total = 0

while i <= 10:
    total = total + i   # add current i to total
    i += 1

print("Sum =", total)  # print final sum    