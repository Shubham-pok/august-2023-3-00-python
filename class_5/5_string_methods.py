
message = 'hello world '

#capitalize()
result = message.capitalize()
print(result) #Hello world

#title()
result= message.title()
print(result)



#upper()
result=message.upper()
print(result) #"HELLO WORLD"


#lower()
result= message.lower()
print(result)#

#split
message = "hello world "
result = message.split()
print(result) #['hello', 'world']


message= "i,am,learning,python"
result = message.split(',')
print(result) #['i','am',learning', 'python']

message="hello world "
result= message.split("o")
print(result)#['hell',' w', 'rld']


#join()
data= ['hell',' w', 'rld']
result="o".join(data)
print(result)


data = ["hello ","world"]
result=" ".join(data)
print(result) # "hello world"


#find ()
message ="hello world"
result= message.find("w")
print(result) #6


message ="hello world"
result= message.find("orl")
print(result) #7


#if we gives the subsets not prevent in the string then find() return -1


#replace ()
message="hello world"
result=message.replace("hello","HELLO")
print(result) # HELLO world


message="hello world"
result=message.replace("hello world","HELLO  WORLD ")
print(result)
