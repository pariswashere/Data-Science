a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while x != y:
    if x < y:
        x += a
    else:
        y += b

print("LCM:", x)