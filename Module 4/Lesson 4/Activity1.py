number =  int(input("Enter the number : "))
digits = len(str(number))
sum = 0
temp = number

while temp>0:
    digit = temp%10
    sum = sum + digit**digits
    temp = temp//10

if number == sum:
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")