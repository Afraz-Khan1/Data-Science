str=[1,2,3,4,5,7,8] #printing the elements of list
for it in str:
    print(it)
 
for it in str:
    if it==4:
        print("found")
        break
    else:
        print("not else here")
else: # if for loop didn't return any thing or condition was not true in any case
    print("not found")

str1=(1,2,3,4,5,49,42) # finding an element in tuple
for it in str1:
    if it==49:
        print("found")
        break
else:
    print("not found") 

# range() function that can be used to print the element within a range. for example:
# range(1,5) will return 1,2,3,4
# range(5) will return from 0to4
# range(1,10,2) will return 1,3,5,7,9 : that 2 means jump only one element after one print.

for el in range(2,11,2): # printing all even numbers
    print(el)  

# printing the table using range funtion:

x=int(input("Enter number to print its table upto 10: "))

for i in range(1,11):
    print(x," x ",i," = ",x*i)

# calculate the sum of n numbers:
n=int(input("Enter number to calculate sum upto number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum Upto given number is : ",sum)

# to calculate factorial of given number:

n=int(input("Enter number to calculate its factorial:"))
fact=1
#for el in range(1,n+1):
 #    fact*=el
#print("Factorial of given number is: ",fact)

# second method  using while loop more easy

i=1
while i<=n:
    fact*=i
    i+=1
print("factorial: ",fact)

# now its time to learn functions: 

def cal_avg(a,b,c):
    return (a+b+c)/3

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
avg=cal_avg(a,b,c)
print(avg)

# now its time to learn recurrsion:

# write a function to calculate factorial of a number using recurrsion concept:
def cal_fact(n):
   if n==1:
    return 1
   return cal_fact(n-1)*n
   
n=int(input("Enter number to calculate its factorial using recurrsion concept: "))
print(cal_fact(n)) 

# how this recursion works here:
#1) call stack is here: first call starts number i.e 4. 4 says no i want factorial of n-1 first than i multiply n
#2) than same goes for number 3 it says no i want factorial of 3-1=2 first than i multiply n
#3) at last when n==1 it return 1 and number 2 multiply 1 by 2 and 2 is multiplied by 3 and than 6 multiplied by 4 and ans comes 24
# for number 4.

# write a recursive function to calculate the sum upto n numbers:
def cal_sum(n):
    if n==1:
        return 1
    return cal_sum(n-1)+n

n=int(input("Enter number to calculate its sum using recurrsion concept: "))
print(cal_sum(n))

#write a recursive function to print all the elements in the list:

def cal_print(list,length=0):
    if length==len(list):
      return
    print(list[length])
    cal_print(list,length+1)
    
cities=["karachi","peshawar","hyderabad","quetta"]
length=len(cities)
cal_print(cities)