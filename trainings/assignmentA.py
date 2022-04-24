# Assignment ##
# 1. Write Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a = 50
b = 20
print ("variable a", b)
print ("variable b", a)

a = float(input("give your a variable value: "))
b = float(input("give your b variable value: "))

print ("variable value b", b)
print ("variable value a", a)

# 2. Write a Program for computing area and circumference of circle.
# 2 · π · r (2 * π * r)
π = 3.14
r = 10
CT = 2
print ("circumference of a circle is equal to", (CT*π*r))

π = float(input("Enter pi value: "))
r = float(input("Enter Raduis: "))
CT = float(input("Constant number: "))
print ("circumference of a circle is equal to", (CT*π*r))

# print("--------------------------------END----------------------------------------")
# Write a Program for note denomination in 2000 , 500 and 100.
notes = (2000,500,200,100,50,20,10,5,2,1)
amount = float(input("Enter Amount to be paid : "))
amount = int(input("Enter Amount to be paid : "))
# amount = 3000
for n in notes:
    count = amount//n
    print("Note Value : ", n,'\tnumber of notes ',count)
amount = amount%n

# Write a Program to calculate the simple interest given in all the required values.
principle=float(input("Enter the principle amount:"))
time=int(input("Enter the time(years):"))
rate=float(input("Enter the rate:"))

simple_interest=(principle*time*rate)/100
print("The simple interest is:",simple_interest)

# Write a Program to calculate the total and average of 5 subject marks
maths = 10
english = 3
chemistry = 5
physics = 8
python = 60
sum = (maths+english+chemistry+physics+python)

print ("sum of subject marks", sum)
print ("sum of subject marks", sum/5)

english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
python = float(input("Please enter python Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + math + python + physics + chemistry
average = total / 5
percentage = (total / 5) * 100

# print("\nTotal Marks = %.2f"  %total)
# print("Average Marks = %.2f"  %average)
# print("Marks Percentage = %.2f"  %percentage)

print ("total number of subject marks", total)
print ("average subject marks", average)
print ("percentage of subject marks", percentage)