# Assignment 2 ###
# Write a program that takes a string and replaces every blank space with a hyphen.

greeting = "Good Morning Class"
greeting = greeting.replace(' ','-')
print (greeting)

greeting = input("Enter greeting: ")
greeting = greeting.replace(' ','-')
print (greeting)

# Write a program takes a string and swaps the first character and the last character of the string.
stringvalue= input("Enter string: ")
print(stringvalue[-1]+stringvalue[1:4]+stringvalue[0])

# Write a program takes a string and replaces all occurrences of ‘a’ with ‘$'
value = input("Enter string: ")
value = value.replace('a','$')
print (value)

# Write a program to calculate the no. of character in string given by user
value = input("Enter string: ")
value = len(value)
print (value)

str1 = input("Please Enter your Own String : ")
total = 0

for i in range(len(str1)):
    total = total + 1
print("Total Number of Characters in this String = ", total)

# Write a program to count a char (‘i’) in given string by user.
value = input("Enter string: ")
value = value.count('e')
print ("Count of e in string is : " +  str(value))

value = input("Enter string: ")
value = value.count("e")
print ("count of e in string is: ", value)


# Write a program to split the string given by user by the space.
value = input("Enter string: ")
value = value.split()
print ("split string is: ", value)
