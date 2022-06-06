# my_list = [2,4,6,8,10,34,75,19,39,10,50,67,20,57,28,46,18,39,80]

# for value in my_list:
#     rem = value % 2
#     if rem == 0:
#         print(f"{value} is even")
#     else:
#         print(f"{value} is odd")

# Read a string and print character with index values.

user_string = input("enter a string here: ")
index = 0

for value in user_string:
    print(f"{user_string} ----> {index}" )
    index = index + 1