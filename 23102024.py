# TYPES OF ARGUEMENTS 

# * 1.POSITIONAL ARGUMENTS

# positional arguements we Pass the values to the function call without variable name
# while passing values we need to follow order...no of arguements in function call and function declaration both has to be same.

def greet(s1,s2):
    print(s1+s2)

greet(10,20)
greet("hbd" , "krishna")


# * 2.KEYWORD ARGUEMENTS

# keyword arguements we pass the values in function call with specific variable name
# no.of arguements in function call and function declaration both has to be same.

def details(name,age,gender):
    print(f'name:{name}')
    print(f'age:{age}')
    print(f'gender:{gender}')   

details(age='24',gender='male',name='pradeep') 

# * 3.DEFAULT ARGUEMENTS

# it takes default value when there is no value passed in function call
# no.of arguements in function call and function declaration no need to be same


def sample(a=0,b=0,c=0):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')

sample(10,20,30)
sample('*',30)


# VARIABLE LENGTH KEYWORD ARGUEMENT

# it allows a function to accept any no.of keyword arguemnts.and it stored in the form of dictionary.
# variable name prefixed with **

def sample(**kwargs):
    print(f'kwargs:{kwargs}')

sample(a=10,b=20,c=30)
sample()