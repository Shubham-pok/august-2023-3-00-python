# Encapsulation is the process of data hiding in the OOP approach of programming
# We can create public, private and protected members of a class in most of the OOP languages
# In Python, protected members are created using a single underscore, private members are created
# using a double underscore and public members do not contain any underscores

class Vehicle:
    __engine_type = "petrol"  # private member

    def __init__(self, color, doors):
        self._doors = doors   # protected member
        self.color = color  # public

    def _description(self):
        return f"Vehicle has {self._doors} doors and {self.color} color"

    @property
    def engine_type(self):
        return self.__engine_type

    def set_engine_type(self, e_type):
        self.__engine_type = e_type


class Bike(Vehicle):
    def description(self):
        return super()._description()