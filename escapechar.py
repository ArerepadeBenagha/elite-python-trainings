splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# First one use's a single string and then escapes with a backward slash in between the words
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# First one use's a double string and then escapes with a backward slash in between the words
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print()
# First one use's a triple string and then escapes with a backward slash in between the words
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")


# anotherSplitString Example

anotherSplitString = """This string has been
split over
several
lines"""

# basically this code is using the tabbedString to space out the words as appear like so
print("Number 1\tThe Larch")
print('Number 2\tThe Horse Chestnut')

# trying to override already existing function type in python from this example
# print("C:\Users\tim\notes.txt")
print("C:\\Users\\tim\\notes.txt")    # But this is a preferable solution

# Or
print(r"C:\Users\tim\notes.txt")

