#We can create a file,read,update and delete the content of the file using Python Language
#file can be opened in following modes in python
#r=> Read mode
#w=> write mode
#a=>append mode
#r+ => read and write mode
#w+ => write and read mode
#x=> exclusive write mode

filename = "message.txt"
fp=open(filename,"w")
fp.write("Hello World")
fp.close()

fp=open(filename,'r')
data=fp.read()
print(data)
fp.close()

fp=open(filename,'a')
try:
    fp.write("\n i'm learning python ")
finally:
    fp.close()

#Opening the file with the above method can be problematic sometimes as we may forget to close the file
#so, it is better to open your file using context manager

with open(filename,'r') as fp : #context manager
    data=fp.read()
print(data)


with open(filename,"r+") as fp:
    data = fp.read()
    fp.write("\nPython is a high level language ")
print(data)

# with open(filename,"w+") as fp:
#     fp.write("i'm learning python")
#     data=fp.read()
# print(data)



