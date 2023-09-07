#There are broadly two types of error in any programming language :
#1.syntactic Error
#2. NON-syntactic Error


#1.Syntatical Error
#this types of error occurs when we mess up with the grammar of the programming language
#Example
#a= #Incomplete code
#if a:
#print("a") #if blocks without Indentification etc are the syntax error of python language


#2.Non-syntactic Error
#All other error except syntax error fail in this category
#these error can further be classsified as
#1.Type Error
#2.Value Error
#3.Zero Division Error
#4.Name Error
#5.Modules method Error
#6. Index Error
#7.key Error

#2 +"Hello" #TypeError
#int("Hello") #value Error
#3/0 #zerodivision Error

#a= 1
#print(b) #Name b is not defined .Name Error

#Import jason # no module name jason .ModuleNOtfoundError

#a= [1,2,3,4]
#print (a[5]) #Index Error


student = {"name": "ABC", "age": 20}
print(student["id"])   # KeyError
print(student.get("id"))  # None