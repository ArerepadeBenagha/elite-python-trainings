answer = 5
print("Please guess from the range of numbers 1 and 10: ")
guess = int(input())

if guess < answer:
    print("print guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")

