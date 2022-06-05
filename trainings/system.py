import os
import platform

if platform.system() == "linux":
    os.system("clear")
    print("screen clear for linux machine done")

elif platform.system() == "windows":
    os.system("cls")
    print("screen for windows cleared and done")

else:
    print("this script was not copied to a linux or windows machine")