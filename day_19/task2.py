#Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
# Add the radius of the circles and print the result.
#Do the above task using a method and then a magic method.
#Compare the size of the circle and print the result using magic method.

class circle:
    def __init__(self,radius):
        self.radius = radius

    def sum_get(self,other):
        return self.radius + other.radius

    def __add__(self,other):
         return self.radius + other.radius

    def __gt__(self, other):
        return self.radius > other.radius

c1= circle(20)
c2 = circle(30)

result = c1.sum_get(c2)
print(result) # 50

total = c1 + c2
print(total) # 50


outcome = c1 > c2
print(outcome) #True/False

