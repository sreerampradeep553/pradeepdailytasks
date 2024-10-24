### """BASIC LIST OPERATIONS"""
## """1.Write a Python program to create a list of 5 integers and print the sum of all elements in the list."""

a=[11,12,13,14,15]
total_sum = sum(a)
print(total_sum)


##"""2.Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing."""

fruitnames=['banana','apple','grape','guaua','papaya']
print(fruitnames[1])
print(fruitnames[3])

##"""3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list."""

numbers =[1,2,3,4,5,6,7,8,9,10]
print(numbers[:3])
print(numbers[-3:])
print(numbers[::2])

### """2. Adding and Removing Elements"""

## """.Write a Python program that initializes a list with some numbers and:"""


a=[i for i in range(10,51,10)]
print(a)

## """2.Adds a new number to the list using the append() method."""


a=[5,10,15,20,25]
a.append(30)
print(a)


## """3.Inserts a number at the second position using insert()."""

a=[10,20,30,40,50]
a.insert(1,25)
print(a)


## """4.Extends the list with another list of numbers."""

abc=[15,25,35,45,55]
abc.extend([20,30,40,50])
print(abc)

## """ 5.Remove all occurrences of the number 3 from a list of integers."""

xyz=[13,3,26,3,33,45,56]
for l in range(0,len(xyz)):
    if xyz[l] !=3:
        print(xyz[l])


## """6.Write a Python program to remove the last element of a list using pop() and print the updated list."""


s=[100,200,300,400,500,600]
m=s.pop(-1)
print(m)

## """3. Sorting and Reversing Lists:"""

## """1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse()."""

ijk=[56,46,78,72,23,45,63,12,97,34]
ijk.sort()
print(ijk)
ijk.sort(reverse=True)
print(ijk)


## """2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results."""

sky=["hello","hiii","welcome","good","bad"]
sky.reverse()
print(sky)
print(sky[::-1])

## """4. Aliasing and Cloning:"""

## """1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list."""


old=[1,2,3,4,5]
new=old.copy()
print(new)
old.append(6)
print(old)


## """2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not."""


a=[1,2,3,4,5]
alias_list=a.copy()
print("a:",a)
print("alias list:",alias_list)

a.append(6)
print("a:",a)
print("alias list:",alias_list)

alias_list[0]= 10







## """5. Mathematical Operations:"""


## """1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times."""


a=[1,2,3]
b=[4,5,6]
print(a+b)
c=a*3
print(c)


## """2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2)."""


a=[1,2,3,4,5]
b=[num * 2 for num in a]
print(b)



## """6. Membership Operators:"""


## """.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found.""""


a=[1,2,3,4,5,6,7,8,9,10]

if 5 in a:
    position=a.index(5)
    print(f"element 5 found at position  {position}.")
else:
    print(f"element 5 is not found.")



## """Given a list of student names, check if "John" and "Sara" are in the list using the in operator."""


names=["hello","john","world","welcome","sara"]
if "john" in names:
    print("john is in the list.")
else:
    print("john is not in the list.")

if "sara" in names:
    print("sara is in the list.")
else:
    print("sara is not in the list.")



## """7.Nested Lists:"""


## """1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3."""


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for row in matrix:
    print(row)

row = 2
column = 2
element = matrix[row-1][column-1]
print(f"/n Element at row {row},column{column}:{element}")


### """2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade."""


lsg=[["pradeep",90],["balaji",86],["moksha",89]]
for student in lsg:
    name = student[0]
    grade =student[1]
    print(f"Name:{name},Grade:{grade}")


### """8. Advanced Challenges:"""


## """1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:One containing only the even numbers.Another containing only the odd numbers."""



numbers = list(range(1,21))
even_numbers=[num for num in numbers if num%2!=0]
odd_numbers=[num for num in numbers if num%2==0]
print("EVEN NUMBERS",even_numbers)
print("ODD NUMBERS",odd_numbers)



## """2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates)."""



a=[2,4,7,3,4,2]
b=list(set(a))
print(b)



## """Given a list of tuples representing (name, age), sort the list by age in ascending order."""


a=[("pradeep",20),("balaji",15),("moksha",25)]
b=sorted(a,key=lambda x:x[1])
print("sorted list:")
for person in b:
    print(f"name:{person[0]},age:{person[1]}")
