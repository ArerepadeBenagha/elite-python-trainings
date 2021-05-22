a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after  interger divison

for i in range (1, 4):
    print(i)

# for i in range (1, a / b):
#     print(i)

for i in range (1, a // b):
    print(i)
