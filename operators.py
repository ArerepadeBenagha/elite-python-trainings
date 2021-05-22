a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b) # integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after  interger divison

for i in range (1, 4):
    print(i)

# for i in range (1, a / b):
#     print(i)

for i in range (1, a // b):
    print(i)



# You have a shop selling buns for $2.40 each. A customer comes in with $15, and would like to buy as many buns as possible.
# complete the code to calculate how many buns the customer can afford.
bun_price = 2.40
money = 15

print(money / bun_price ) # 6.25, so the customer can buy 6 buns with 0.25 as remainder

print(money // bun_price ) # 0 modulo returns no remainder , so the customers get 6 buns


# Operator Precedence
print(a + b / 3 - 4 * 12)       # doesn't follow bodmas
print(a + (b / 3) - (4 * 12  )) # doesn't follow bodmas

print((((a + b) /3) - 4) * 12)
print(((a + b) /3 - 4) * 12)


# Use variables to hold the values
c = a + b
d = c / 3
e = d - 4
print (e * 12)
