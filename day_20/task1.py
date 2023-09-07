#Take two numbers as input and add those numbers. Handle the possible exceptions.



try:
    num1= int(input("Enter first number: "))
    num2=int(input("Enter second number:"))
except ValueError:
    print("Input a number, not character")
else:
    print(num1)
    print(num2)
    print(num1+num2)
