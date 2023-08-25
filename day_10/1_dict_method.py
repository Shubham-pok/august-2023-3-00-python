#popitem()
student = {"name": "jon", "age":30,"address":"KTM" }
result = student.popitem()
print(result)
print(student)


#clear()
student = {"name": "jon", "age":30,"address":"KTM" }
student.clear()
print(student)


del student #it deletes the student objects
#print(student) # NameError


#copy()
student= {"name": "jon", "age":30,"address":"KTM" }
student1= student.copy()
print(student)#{"name": "jon", "age":30,"address":"KTM" }
print(student1)#{"name": "jon", "age":30,"address":"KTM" }



#get()
student= {"name": "jon", "age":30,"address":"KTM" }
name = student.get("name")
print(name) #"jon"
phone= student.get("phone")
print(phone) # NONE
phone= stuudent.get("phone",9898080898)
print(phone)
name = student.get("name","jane")
print(name)


#keys
student= {"name": "jon", "age":30,"address":"KTM" }
keys = student.keys()
print(keys)#dict_keys (["name","age","address"])


#values
values = student.values()
print(values) #dict_values(["jon",30,"KTM")

#items
items = student.items ()
print(items) #dict_items(["name","jon") ,("age","30"),("address","KTM")

items = list (student.items())
key,value = items[0]
print(key)
print(value)


#from keys
y={}
result = y.fromkeys([1,2],"Hello")
print(y)
print(result)
result = y. fromkeys([1,2])
print(result)


# setdefault()
student = {"name": "Jon", "age": 30, "address": "KTM"}
student.setdefault("phone", 9890989878)
print(student)
student.setdefault("name", "Jane")
student.setdefault("phone", 9890989879)
print(student)