l = int(input("Enter the largest number : "))
s = int(input("Enter the smallest number : "))

while(s):
    x = s
    s = l%s
    l = x 

print("HCF : ",l)
