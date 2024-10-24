### Write a python program to merge two list? ##

l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1+l2) # result= [1, 2, 3, 4, 5, 6, 7, 8]


### Write a python program to delete element of given index in list ? ##

a=[1,2,3,3,4,5]
s=a.pop(2)
print(s)  #result=3


### Write a pytho program to delete given element from the list? ##

a=[10,20,30,40,50]
a.remove(40)
print(a) #result= [10, 20, 30, 50]

### Write a python programe to check if the two list are having atleast one common element?

a=[10,20,30,40,50]
b=[30,60,70,25,35]
c=a==b
print(c)


### Write a python program to remove  specified column from the nestedlist? ##

z=[100,200,300,400,[10,20,30,40,[1,2,3,4]]]
k=z.pop(4)
print(k)

### Write python program to convert a list of integers into single integer ?



### Write  a python programe to remove duplicates from the list ?



### Write a program to create a set.

a=set()
print(type(a))  # Empty set

a={1,2,3,4,5}
print(type(a))  # with values set


### Write program to iterate over sets.

a={1,2,3,4,5}
for b in a:
    print(b)


### Write a Python program to add member to a set.


a={10,20,30,40,50}
a.add(25)
print(a)


### Write a Python program to remove item from a given set.

a={10,20,30,40,50}
a.remove(30)
print(a)


### Write a python program to create a intersection of set ?

a={10,20,30,35,45}
b={15,25,35,45,55}
k= a & b
print(k)


### Write a python program to createa unionof set ?

a={1,2,3,4,5,6}
b={6,7,8,9,0}
c= a|b
print(c)


### Write a python program to create set differance ?

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}
c= a-b
print(c)

### Write a python program to create a symmetric defferance ?

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}
c= a^b
print(c)

### write a python program to find max and min values in a set?

a={1,2,3,4,5,6}
print(max(a))
print(min(a))

### Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}

a= a-b
print(a)

### Write a Python program to remove items 10, 20, 30 from the following set at once.?

a={10,20,30,40,50,60}
b=(10,20,30)
a.difference_update(b)
print(a)

### Check if two sets have any elements in common. If yes, display the common elements?

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}
if a & b:
    print("common elements",a & b)
else:
    print("no common elements")

### update set1 by adding items from set2, except common items?

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}
a=b-(a&b)
print(a)

### Remove items from set1 that are not common to both set1 and set2?

a={1,2,3,4,5,6}
b={6,7,8,9,5,4}
a &= b
print(a)

### How do you create a empty tuple on python ?

a=()
print(type(a))

### Write a python program to unpack atuple into several variables ?

marks=(48,64,87,75)
b,c,d,e=marks
print(b)
print(c)
print(d)
print(e)

### write a python program to add an item to the tuple ?

a=(35,46,57,68)
b=list(a)
b.append(40)
a=tuple(b)
print(a)


### Write a python proram to convert tuple into a string ?

a=("hello pradeep")
b="".join(a)
print(b)

### Write a python program to find most frequent element in tuple ?


print("==========================================================================================")

### Write a python program to  add a key to a dictionary ?

a={"name":"pradeep","age":30}
print(a)


### Write a python program to check weather the given value is present in the dictionary or not ?

a={"name":"pradeep","age":30,"city":"kadapa"}
value="pradeep"

if "pradeep" in a.values():
    print(f"{value} is present in the dictionary.")
else:
    print(f"{value} is not present in the dictionary.")

