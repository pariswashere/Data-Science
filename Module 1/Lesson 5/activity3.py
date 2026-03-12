x = int(input("Enter a number : "))
y = int(input("Enter a number : "))


def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Sum :", add(x,y))
print("Difference :", substract(x,y))
print("Product :", multiply(x,y))
print("Quotient :", divide(x,y))