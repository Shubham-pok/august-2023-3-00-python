#string formatting in Python can be done with three methods
#1.f-strings
#2.format specifier
#3.format() mehod



#f-mothod
name = "jon"
message=f"Hello I'm {name}"
print(message) # Hello I'm jon




#.format () mehod

name="jane"
language= "python"
message = "Hello I'm {}. I'm learning {}".format(name,language)
print(message)

#format specifier
name= "jane"
language= "python"
age= 21
message = "Hello I'm %s.I'm learning %s. I'm %d " % (name,language,age)
print(message)




