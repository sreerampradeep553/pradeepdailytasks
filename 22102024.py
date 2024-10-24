## DAILY TASK 22102024

# without using inbuilt function len(), we can find the length of the variable..?

l=[1,2,3,4,5,6,7,8,9,0]
j=0
for i in l:
    j= j+1

print(j)


 ## --> For checking it is true or not

# Inbuilt Functions
 # -->Inbuilt functions or predefined functions are already developed by the developers


# RECURSIVE FUNCTION 

# --> Function calling it self is called recursive function

# Factorial program

def factorial(z):
    if z == 0:
       return 1
    else:
       return(z* factorial(z-1))

print(factorial(4))


# LAMBDA FUNCTION  SYNTAX --> lambda arguements : expression


l=lambda x : x*x
print(l(4))


# written the greatest among two numbers using a lambda function ?


l= lambda x,y : x if x>y else y
print(l(200,300))


# FILTER FUNCTION :- sYN --> filter(function,sequence)

# --> filter function will returns the filter object



def get_evens(l):
  if l%2 == 0:
      return True
  else:
      return False


l=[1,2,3,4,5,6,7,8,9]
f=filter(get_evens,l)
print(list(f)) # type casting using for confirmation

# REDUCE FUNCTION :- sYN --> variable name = reduce(lambda x,y : x+y)

# From Functools 
from functools import reduce

l=[1,2,3,4,5,6,7,8,9,0]
rs=reduce (lambda x,y :x+y,l)

print(rs)


# MAP FUNCTION  

def sqr(l):
  return l*2


l=[1,2,3,4,5]
m=map(sqr,l)
print(list(m))
