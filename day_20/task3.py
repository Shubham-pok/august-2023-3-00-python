#Create a dictionary student with keys id, name, age, department. Take a input from the user,
# which info (id, name, age or department) he wants to access and print the result. Handle the possible exceptions.

Student = {"id": 12 , "name": "hari","age": 20,"department":"IT"}
try:
    key = input("Enter the info you want to get ")
    result = Student[key]

except  KeyError:
    print("plz provide the valid key")
else:
    print(f"the {key} of the student is {result}")
