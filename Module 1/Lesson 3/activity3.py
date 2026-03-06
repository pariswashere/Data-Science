num = int(input("Enter a number : "))

if num>50:
    print("The number is greater than 50.")
    if num%2 == 0:
        print("It is even too.")
    else:
        print("It is odd too.")
        
else:
    print("The number is less than 50.")