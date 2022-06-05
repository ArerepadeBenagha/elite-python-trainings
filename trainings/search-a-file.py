# linux
# import os
# required_file = input("Enter desired filename to search: ")

# for x,y,z in os.walk("/home/devopslab/elite-python-trainings/trainings"):
#     for each_file in z:
#      if each_file == required_file:
#         print(os.path.join(x, each_file))

# windows
# import os
# required_file = input("Enter desired filename to search: ")

# for x,y,z in os.walk("C:\\Users\\lbena\\OneDrive\\Documents\\Github"):
#     for each_file in z:
#      if each_file == required_file:
#         print(os.path.join(x, each_file))

# Because we can get the system path very easy with windows as there is in linux we have to come up with a logic

# import os
# import string

# required_file = input("Enter desired filename to search: ")
# drives_names = string.ascii_uppercase
# #print(drives_names)
# valid_drives_names = []

# for each_drive in drives_names:
#     #print(each_drive)
#     if os.path.exists(each_drive + ":\\"):
#         print(each_drive)
#         valid_drives_names.append(each_drive + ":\\")
# #print(valid_drives_names)
# for each_drive in valid_drives_names:
#     for x,y,z in os.walk(each_drive):
#         for each_file in z:
#             if each_file == required_file:
#                 print(os.path.join(x, each_file))

# To make this platform indepedent we do this

import os
import string
import platform
required_file = input("Enter desired filename to search: ")

if platform.system() == "windows":
    drives_names = string.ascii_uppercase
    valid_drives_names = []
    for each_drive in drives_names:
        if os.path.exists(each_drive + ":\\"):
            valid_drives_names.append(each_drive + ":\\")
    print(valid_drives_names)
    for each_drive in valid_drives_names:
        for x,y,z in os.walk(each_drive):
            for each_file in z:
                if each_file == required_file:
                    print(os.path.join(x, each_file))
else:
    for x,y,z in os.walk("/"):
        for each_file in z:
            if each_file == required_file:
                print(os.path.join(x, each_file))
