#there are three types of argument in Python function
#1. positional arguments
#2. Default arguments
#3. arbritrary arguments



#1. Position Arguments
#these are the required arguments in function
#values for them most be passed as parameters during funtion call


def addition (a,b ) #here a and b are position arguments
    return a + b

r =addition(2,5)
print(r)
r = addition(a= 2 , b = 5 )
print(r)
r= addition(b=5 , a=2)
print(r)



#2.Default argument
def addition (a, b , c= 10 ) #Here c is the default argument
    return a + b + c


r = addition(3,2)
print(r)#15
r= addition(3,2,c=4)
print(r)#9
r= addition(b= 3, a=9, c= 7)
print(r)


