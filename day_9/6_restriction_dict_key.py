#Dictionary values can be of any datatypes
#But, there is a rule for dictionary keys that they must immutable .
#Dictionary keys can not contain any mutuable type directly or indirectly

data = {1 :"Hello",2:"World"} #valid
data = {2.1:[1,2,3], True:"Hello"} # valid
data = {(1,2,3):1,(4,5):2} #valid

data = {([1,2,3],2):"Hello",2:"World"} #Invalid
data = {[1,2,3],:"Hello",2:"World"} #Invalid

student={"name" : "jon", "address":"KTM"} #valid



#Membership in Dictionary is observed in keys and nit in values
student={"name" : "jon", "address":"KTM"}
print("joh" in student) #Flase
print("name" in student) #True
print("address" not in student)#False

