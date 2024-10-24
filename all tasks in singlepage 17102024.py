#### DATA TYPES   ###
# Data types are used for defining the type of data that we are stored in single VARIABLE...
# Data types are two types....they are 
# 1.single value or numerical data types
# 2.collection value data types..


# """single value or Numerical data types are"""
   #int -->"integer is a number without decimal point.default value is zero"
   #float -->"float is a number with decimal point eg:(10.5)"
   #boolean -->boolean value will have only two values...1.true...2.false.default value is false.
   #complex -->complex will have two parts 1.real...2.imaginary  (eg:2+3j) 2 is real +3j is imaginary

# """declartiopn of int.."""
a=10
print(type(a))

#""declaration of float""

a=10.5
print(type(a))

# "declaration of boolean"
a=True
print(type(a))

# "declaration of complex"

a=3+4j
print(type(a))

print("====================================")



# """CoLLECTION VALUE DATA TYPES..."""

"""1.STRING"""
"""2.LIST"""
"""3.TUPLE"""
"""4.SET"""
"""5.DICTIONARY"""



## """1.STRING"""

###'--> string Is nothing but collection of characters 
###--> we can declare a string In single quotes And double quotes And we declare multiple lines In triple quotes  (eg: ' '," ",'" "')
###--> it supports indexing..it Is ordered data Type
###--> it Is immutable data Type..we cannot change the Data  

#  """"DECLARATION OF STRING"""

a='PRADEEP'
print(type(a))

# """STRING IN BUILT METHODS"""

### --> UPPER CASE () Converting characters into uppercase mode

a='PraDeEp'
b=a.upper()
print(b)


### --> LOWER CASE () Converting characters into lowercase mode

a='PraDeEp'
b=a.lower()
print(b)
### --> SWAP CASE () Converting characters in lowercase to uppercase,uppercase to lowercase mode

a='PraDeEp'
b=a.swapcase()
print(b)


### --> TITLE ()it Converts Every word first letter into uppercase

a='PraDeEp Welcome To India'
b=a.title()
print(b)

### --> CAPITALIZE () converts starting letter of the string into uppercase remaining string converted into lowercase

a='PraDeEp Welcome To INdia'
b=a.capitalize()
print(b)


### INDEX METHOD  

# """It returns index position of first occurance of a given substring.if substring not available it throws value error"""

a="skywaves softwares"
print(a.index('y'))

## RINDEX METHOD

# """It returns index position of last occurance of a given substring.if substring not available then it throws value error"""

a='skywaves softwares'
print(a.rindex('e'))

a='skywaves softwares'
print(a[4])

## FIND METHOD

# if substring is not available then find metod returns -1

a='welcome to the skywaves'
print(a.find('o'))

## COUNT METHOD

# this method returns no of times substring occured in a string

a='Pradeep'
print(a.count('e'))

## REPLACE METHOD

# This method is use to replace one substring with another substring

a='Pradeep sreeram'
s=a.replace('e','@')
print(s)

## JOIN METHOD 

# it is used to join the new things or new characters

a=['sreeram' 'pradeep']
print('@'.join(a))

## SPLIT METHOD

#Split method is used to convert string into list..providing arguement is not mandatory by default it will take space('-') as delimator

a='sreerampradeep'
s=a.split('m')
print(s)

## SLICING

#Slicing is a feature to excess part of sequence from the string,list,tuple.

a='welcome to the world'
print(a[0:3])


### concatination Operater
# -->  for addition of two strings

a='sreeram'
b='pradeep'
print(a+b)


## REputation operator
# --> for multiplying the characters

a='abc'
print(a*3) 

print('=============================================================================')

## KEY WORDS IN PYTHON

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

## CONTROL STATEMENTS

# BREAK
# CONTINUE
# PASS

# BREAK
# --> it takes the control outside the loop.when given condition is satisfied

for c in range(1,11):
   if c==3:
      break
   print(c)
print('outside loop')


## CONTINUE

# --> if control reaches continue it will skip the current iteration and control goes to next iteration

for c in range(1,11):
   if c==3:
      continue
   print(c)
print('outside loop')

## PASS

# --> pass will not affect control flow of a program
# -->it is used to create an empty block other wise it throws syntax error

for c in range(1,11):
   if c==3:
      pass
   print(c)
print('outside loop')


### CONDITIONAL STATEMENTS

# IF CONDITION

# --> control enters inside "if" block.if given condition is true.it will exicute

if True:
   print('currently it is in if block')
else:
   print('in if block')

# ELIF CONDITION

# --> If Previous condition is false then control goes to inside elif block.
# --> for elif block if block is mandatory ,else block is not mandatory

if False:
   print('currently it is in if block')
elif True:
   print('in elif block')
else:
   print('it is in if block')

# ELSE CONDITION

# --> if given condition is false then control goes inside else block
# --> for else block if condition is mandatory

if False:
   print('currently it is in if block')
else:
   print('in Else block')


print("==========================================================================================")



### LIST DATA TYPE

# --> collection of elements in different data types stored in single variable
# --> declared in square brackets "[ ]".elements separated by " , "
# --> it is mutable ,it supports indexing,it is ordered data type.
# --> it allow duplicates

x=[1,2]
print(type(x))

## ADD THE VALUES IN LIST

# APPEND -->This method is used add the one value at the end of the list

l=[1,2,3]
l.append(10)
print(l)


# INSERT --> This method is used to add the one value at certain index position in the list

l=[1,2,3,4,5,6,7]
l.insert(2,9)
print(l)

# EXTEND --> this method is used to add the multiple values at the end of the list in the form of collection value data type

l=[1,2,3,4,5,6,7]
l.extend('pradeep')
print(l)

### REMOVING ELEMENTS FROM THE LIST

# REMOVE METHOD
# --> remove takes value as an arguement,if value occurs more than ones it removes the first occuranceof value in list
#--> if value is not available in list it throws value error


a=[10,20,30,40,50]
a.remove(30)
print(a)

# POP METHOD

# it takes index as an arguement,it returns removed  value
# if index is not given default it takes index as -1

a=[10,20,30,40,50]
a.pop(1)
print(a)


a=[10,20,30,40,50]
a.pop()
print(a)


## Clear Method

# clear method is used to clear the all elements from the list

a=[10,20,30,40,50]
a.clear()
print(a)


### SORTING METHOD

# this method is used to arrange the values in assending order or desending order

l=[90,80,10,20,60,30,40,50]
l.sort()
print(l)

l=[90,80,10,20,60,30,40,50]
l.sort(reverse=True)
print(l)

print("====================================================================================================")

### TUPLE

# # --> collection of elements in different data types stored in single variable
# --> declared in paranthasis "( )".elements separated by " , "
# --> it is immutable ,it supports indexing,it is ordered data type.
# --> it allow duplicates

a=()
print(type(a))

a=(1,2,3)
print(a)



