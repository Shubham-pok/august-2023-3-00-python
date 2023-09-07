#class methods are those methods which takes class as the first argument.
# It doesn't take "self" as a first parameter.it takes 'cls '
#class methods can be useful in creating factory methods


class person:
    def __init__(self,age):
        self.age = age

    @classmethod
    def age_from_year(cls,year):
        age = 2023-year
        return cls(year) #person(31)

    @staticmethod
    def grade(current_grade):
        return f"I study in grade {current_grade}"

p1 = person(25)
print(p1.age)

p2=person.age_from_year(1992)
print(p2.age)

p2 = person.grade(10)
print(p2.grade)

# Here "age_from_year" method is a class method and such type of method is also called as a
# factory method

#static Methods
#static method are those methods which do not changes the state of the class or an object
#we do not pass self or cls in the static methods
# In the above person "grade" is static method
