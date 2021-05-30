# for i in range(1, 13):
#     print("No. {:0} square is {:2} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)
# print("*" * 80)

# name = input("Please enter your name:")
# age = input("How old are you you, {0}? ".format(name))
# print(age)
#
# print()
# name = input("Please enter your name:")
# age = int(input("How old are you you, {0}? ".format(name)))
# print(age)
#
# print()
#
name = input("Please enter your name:")
age = int(input("How old are you you, {0}? ".format(name)))
print(age)
# # Conditions
# if age >= 18:
#     print("""You are old enough to vote""")
#     print("""Please put an X in the box""")
# # else clause
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Impossible are you Enoch in the bible?")
else:
    print("""You are old enough to vote""")
    print("""Please put an X in the box""")
