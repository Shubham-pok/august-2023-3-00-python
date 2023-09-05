
#Create a class Department with parameters name and number_of_students.
#Create a method total_students, which takes object as a parameter and return the total number of students from all departments.


class Department:
    def __init__(self,name,no_of_students):
        self.name=name
        self.no_of_students = no_of_students


    def total_student(self,other):
        return self.no_of_students + other.no_of_students

    def __add__(self, other):
        return self.no_of_students + other.no_of_students


d1 = Department("IT",20 )
d2= Department("CS",30)
total=d1.total_student(d2)
print(total)


result = d1+d2
print(result)

