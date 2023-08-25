a = int( input("enter first number "))
b = int(input("enter second number "))
c = int(input("enter third number"))
if a > b and a > c:
        print(f"{a} is the greatest number ")
elif b > a and b > c:
        print(f"{b} is the greatest number")
else:
    print(f"{c} is the gretest number")

num1 = int(input("Enter first num "))
num2 = int(input("Enter second num "))
num3 = int(input("Enter third num "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")


if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the greatest")
elif num2 > num1:
    if num2 > num3:
        print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")
