import os
required_file = input("Enter desired filename to search: ")

for x,y,z in os.walk("/home/devopslab/elite-python-trainings/trainings"):
    for each_file in z:
     if each_file == required_file:
        print(os.path.join(x, each_file))