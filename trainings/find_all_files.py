#!/usr/local/bin/python3
import os
req_path=input("Enter your directory path: ")

if os.path.isfile(req_path):
  print(f"The given path {req_path} is a file. Please a directory path only")
else:
  all_f_ds=os.listdir(req_path)
  if len(all_f_ds)==0:
     print(f"The given path {req_path} is empty")
  else:
     req_ex=input("Enter the required files extention .py/.sh/.log/.txt: ")
     req_files=[]
     for each_f in all_f_ds:
        if each_f.endswith(req_ex):
           req_files.append(each_f)
     if len(req_files)==0:
        print(f"There are no {req_ex} files in the logcation of {req_path}")
     else:
        print(f"There are {len(req_files)} files in the location of {req_path} with an extention of {req_ex}")
        print(f"files lists are: {req_files}")
