#Take two numbers input and divide a number by another number. Handle the possible exceptions.

try:
    num1= int(input("Enter first number: "))
    num2=int(input("Enter second number:"))
    result = (num1 / num2)

except ValueError:
    print("Input a number, not character")
except TypeError:
    print("Please carry out proper operation")
except ZeroDivisionError:
    print("Please do not divide by zero")
else:
    print(num1)
    print(num2)
    print(result)




