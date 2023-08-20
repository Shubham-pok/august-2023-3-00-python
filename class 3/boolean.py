#true and false are the boolean types in pythin
#true and flase are also the keywords in python


#operation that gives boolean type

a=5
b=10
c=15
#relational operations
print (b>a) # true
print (b!= a) #true
print (b< a ) #false
print (a= c ) # false


#logical operations
print(b>a and a = c ) # false
print(b>a or a==c) # true
print(not true ) # false
print(not false )# true
print(not a ) # false

#membership operation
print(2 in [1,2,3]) # true
print(3 not in [1.2.3]) # false


# identity operation
a = 1
b = 1
print (a==b) #true
print (a is b) #true
a = 123456 #it is created in one memory location
b = 123456#but it is created in another location

print(a==b) 3 #true
print (a is b) #false

#concept of truthy and falsy
 # truly
 #All non-empty datatypes and non-zero numbers are truly values
a = 12
b = 5.7
c = [1, 2]
d = (4, 5)
e = {1, 2}
f = {"name": "jon"}
g = True
print (bool(b)) # true

# falsy
 #All non-empty datatypes and non-zero numbers are truly values
# all these datatypes are truthy datatypes
# we can check the truthiness of the data using
 a=0
 b=0.0
 c=[]
 d=()
 e={}
 f=set {}
 g= False
print (bool(g)) #false




#pyhon booleans are the subclass of the interger class , that means true is 1 and false 0
a=True
b=3
print (a+b) # 4
print ( 70 + false ) #0
print (True + True ) #2




