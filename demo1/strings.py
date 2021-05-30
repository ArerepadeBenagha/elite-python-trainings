print("Today is a good day to learn python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + "world")

# if we want space, we can add that too
# print (greeting + '' + name)

# # Variables
greeting = "Hello"
name = "Bruce"
# name = input("Louis Benagha")

print(greeting + name)
print(greeting + '' + name)

age = 24
print(type(age))

age_in_words = "2 years"

# print(name + " is " + age + " years old ")
print(name + " is " + "age" + " years old ")
print(type(age))

# Using the f-string
print()
print(name + f" is {age} years old")
print(name + f" {age_in_words} old")

print()
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"pi is approximately {pi:12.50f}")


