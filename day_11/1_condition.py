#Conditions are used to make Logical decision in a programs
#there are four variation of conditions of python
#1.simple if
#2.if else statement
#3. if ---elif statement
#4 Nested if




#1. simple if
# If statement takes truthy or falsy value with it . If the value is truthy then the statement inside
#if blocked is excuted else it is not executed
a= 5
b= 10
c= 15
d= 0

    if b > a:
        print("b is greater than a")

    if b:
        print("b is non-zero")

    if d:
        print("d is non-zero")

    # 2. if...else statement
    if b > a:
        print("b is greater than a")
    else:
        print("a is greater than b")

    if d:
        print("d is non-zero")
    else:
        print("d is zero")

 # 3. if...elif...else
 if a > b:
     print("a is greater than b")
elif a > c:
     print("a is greater than c")
    elif b > c:
        print("b is greater than c")
    else:
        print("c is the greatest")
        
        
4.  NESTED IF 

if c> b : 
    if c>b:
        print("c is the gretest ")
    else:
        print("c is not be the greatest ")
       
else:
    print("b is the gretest ")


#we can also create one- line conditions . this one linear condition is called ternary if
print("a is greater " if a > b else print("b is greater "))