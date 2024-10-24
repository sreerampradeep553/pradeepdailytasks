# 1."""Python program to count occurance of a given characters in string"""

d='engineering'
count=0
res=''
for x in range(0,len(d)):
    if d[x] not in res:
        res+=d[x]
        print(f'{(d[x])} = {d.count(d[x])}')

 # 2."""Python Program to check if two Strings are Anagram""" 
 
# 3."""Python Program to check a string is palindrome or not"""


z='malayalam'
res=''
for y in range(-1,-(len(z)+1),-1):
    res=res+z[y]
if z==res:
    print('palindrome')
else:
    print('not palindrome') 


# 4."""" Python program to replace the string space with a given character. """


string = "welcome to the world"
char = input("enter char to replace spaces: ")
result =""
for n in string:
    if n == " ":
        result += char
    else:
        result += n
print("Modified String: ",result)


# 5.Python Program to replace the string space with a given character using replace() method."""

input_string = input("enter from user: ")
char = input("enter char to replace: ")
result = input_string.replace(" ",char)
print("modified string:",result)


# 6."""Python program to convert lowercase character to uppercase string""" 

l='SreeRam PraDeeP'
k=l.upper()
print(k)

# 7."""python programcto check given character is digit or not using isdigit() method"""

char = input("enter a character: ")
if len(char) ==1:
    if '0' <= char <='9':
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is not a digit.")
else:
    print("please enter a single character.")

# 8."""python program to separate characters in a given string"""

q="sreeram pradeep"
for j in q:
    print(j)

# 9."""Python Program to remove blank spaces from string"""

v="sky waves software"
without_spaces = v.replace(" ","")
print(without_spaces)

# 10."""Python program to concatenate two strings using join() method"""

a='sreeram'
b='pradeep'
c="".join([a+b])
print(c)

# 11."""Python Program concatenate two strings without using join() method."""

a='pradeep'
b='sreeram'
c=a+b
print(c)

# 12."""" Python program to remove repeated character from string. """"

f='pradeep'
rc=''
for i in range(0,len(f)):
    if f[i] not in rc:
        rc=rc+f[i]
print(rc)

# 13."""Python program to count alphabets,digits and special characters."""

ads="a1! 7sfgfesu679b2@c3#"
a=0
d=0
s=0
for char in ads:
    if char.isalpha():
        a +=1
    elif char.isdigit():
        d +=1
    elif not char.isspace():
        s +=1
print(f"a:{a}")
print(f"d:{d}")
print(f"s:{s}")

# 14. """Python program to check given character is digit or not"""

char = input("enter from user: ")
if char.isdigit():
    print(f"'{char}' is a digit")
else:
    print(f"'{char}'is not a digit")

# 15."""Python program to print all non repeating character in a string."""

string ='sreerampradeep'
for char in string:
    if string.count(char) ==1:
        print(char)

# 16."""Python program to copy one string to another string."""

a="sreeram pradeep"
b=a
print(b)

# 17."""Python program to print the highest frequency character in a string."""

a="Sreeram Pradeep"
max_char = max(set(a),key = a.count)
print(f"Highest frequency char: {max_char}")
print(f"Frequency: {a.count(max_char)}")

# 18."""Python program to calculate sum of integers in string."""

a="a1b2c3d4"
sum_of_inti = 0
for char in a:
    if char.isdigit():
        a += int(char)
print("sum if integers: ",sum_of_inti)
