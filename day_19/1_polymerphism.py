#polymorphism refers to many forms.
#In python ,it refers to different forms of functions and objects.
#len(),sum(),min(),max(),'+' operators ,'-'operator etc shows polymorphism in python.



#In ploymorphism, we mainly study about function/method overloading and operators overloading



#Function overloading
#Fucntion /method overloading occurs when the same function with the same name is defined multiple times
#other OOP language like C++ ,Java may support function /method overloading but Python doesn't support function overloading

# def addition(a, b):
#     return a + b

def addition(a, b, c=0):
    return a + b + c


r = addition(2, 3)  # Error
print(r)
r = addition(2, 3, 4)  # 9
print(r)



#we can give the taste of function overloading by using default argument and *args and **kwargs in
#python .but ,we can't say python supports function overloading

class Vehicle:
    category = 'petrol'
    def description(self):
        return f"Vehicle has {self.category} type"

    def description(self):
        return f"Vehicle engine is of {self.category} type"

v = Vehicle()
print(v.description())

# This example shows that, method overloading is also not possible in Python

