import sys

if len(sys.argv) != 3:
    print("usage:")
    print(f"{sys.argv[0]} <your_required_string> <lower|upper|title>")
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_str == "lower":
    print(usr_str.lower())

elif usr_action == "upper":
    print(usr_str.upper())

elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid. Please select valid options from the list :lower/upper/title")