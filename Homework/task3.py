#write a python program to check whether the input number is prime number or not

def is_prime(number):
    if number <=1 :
       return False

    for divisor in range (2,int(number ** 0.5)+1):
        if number % divisor == 0 :
            return False

    return True

num = int(input("Enter a positive interger: "))
if is_prime(num):
    print(f"{num} is a prime number ")
else:
    print(f"{num} is not a prime number")