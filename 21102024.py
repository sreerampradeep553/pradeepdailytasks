## functions 

# Functions are two types they are..1 predefined Functions --> previously developers will developed the functions and stored it.
# 2 User defined Functinos  --> creating by user for their uses

# function is nothing but it is a organaized block of reusable code.it executes when we call the function. it is declare in by using def keyword.we passing the data to this as an arguements.

def wish(name):
    print("hi hello good morning",name)


wish("krishna")
wish("Pradeep")
wish("Balaji")


def add(x,y):
    print(x+y)
    #print(x*y) -->string is not supported for multiplication

add(100,200)
add(20,30)
add('hii','hello')


### RETURN 

# --> return is keyword that is used to return the values to the function call
# --> we can return multiple values by using return keyword.it takes control from functional space to main space.

def sum(a,b,c):
    return a+b+c


print(sum(1,20,30))
print(sum(1,2,3))
print(sum(100,200,700))