# import os
# print(os.getcwd())

# Execute linux command with system

# print(os.system("ls -l"))
# print(os.system("pwd"))
# print(os.system("touch random.txt"))
#
# cmd = "date"
# x = os.system(cmd)
#
# if x == 0:
#     print("your command ran successfully")
# else:
#     print("your command failed")

# script to clear screen for both windows and linux machine #

import os
import platform

if platform.system() == "windows":
    os.system("cls")
    print("screen clear for windows machine done")

else:
    os.system("clear")
    print("screen clear for linux machine done")
