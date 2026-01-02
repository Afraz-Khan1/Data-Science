collection={}
collection[input("enter subject name: ")]=int(input("enter subject marks: "))
# or use update method.
subject=input("Enter subject: ")
collection.update({subject:int(input("enter marks: "))})
collection.update({input("Enter subject: "):int(input("enter marks: "))})
print(collection)

# store 9 and 9.0 as different values in a set.

#first way
collection1={9.0,"9"}
print(collection1)
#reverse
collection2={"9.0",9}
print(collection2)
#second way add a tuple in set with each tuple have one data type and one value both in string. as tuples are immutable so they can be added in sets
# but not dictionary and list as they are mutable. sets are mutable cuz you can added elements in sets but sets elements are immutable.
collection3={("float",9.0,8),("integer",9)}
print(collection3)