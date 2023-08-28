#*args and **kwargs are the arbitrary arguments
# these arguments are like the expandable buckets which can take any number of parameters


def addition(*args):
    print(args)
   # print(type(args))
    return sum(args)

print(addition(1,2))
print(addition(1,2,3))
print(addition (1,2,3,4 ))
print(addition(1,2,3,4,5))
#addition(1,2,3,"hello",[1,2]) #(1,2,3,"hello",[1,2])


def addition(**kwargs):
    print(kwargs) # Dictionary {'a' : 2,
    return sum(kwargs.value())
addition(a= 2 , b=3 )
addition(a= 2 , b=3 , c=4)
addition(a=2 , b=3, c=4 , d= 5 )


