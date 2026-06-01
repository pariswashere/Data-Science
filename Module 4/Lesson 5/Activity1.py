num = int(input("Enter the number"))


original_number = num
reversed_number = 0

while num>0:
    digit = num%10
    reversed_number = reversed_number*10 + digit
    num = num//10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")