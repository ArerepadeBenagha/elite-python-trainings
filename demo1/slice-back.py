          #01234567890123456789012345#
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

# Create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the sting to produce edbca
print(letters[4::-1])

# slice the string to produce the last characters, in reverse order
print(letters[:-9:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
