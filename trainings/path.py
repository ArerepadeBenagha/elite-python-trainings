import os
import platform

if platform.system() == "windows":
  os.system("cls")

else:
  os.system("clear")

# x = gives path
# y = gives directories lists
# z = gives files in the directories

path = "/home/devopslab/elite-python-trainings/trainings"
#print(list(os.walk(path)))

print("--------------------------------------------------------------------------")

for x in os.walk(path):
    print(x)

print("--------------------------------------------------------------------------")

for x,y,z in os.walk(path):
   print(x)

print("--------------------------------------------------------------------------")

for x,y,z in os.walk(path):
   print(x,y)

print("--------------------------------------------------------------------------")

for x,y,z in os.walk(path):
   print(x,y,z)

print("--------------------------------------------------------------------------")

for x,y,z in os.walk(path):
    if len(z) !=0:
       print(x)
       for each_file in z:
           print(os.path.join(x,each_file))