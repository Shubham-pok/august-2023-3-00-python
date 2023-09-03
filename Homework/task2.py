def calculate_difference(number):
    difference = abs (number - 17)
    if number > 17:
        return 2 * difference
    else:
        return difference


number = float (input("Enter a number: "))

result = calculate_difference(number)

print("The result is :",result)
