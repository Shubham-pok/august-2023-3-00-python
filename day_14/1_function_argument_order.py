#Function arguments has a certain order in PYthon . Following is the order of arguments :
#1.positional
#2. Default /keyboard
#3.*args
#4. **kwargs


def additional (a,b,c=1 ,*args,**kwargs) # Order of arguments in function definition
    pass


def addition(a, b, c, d=1, e=2, *args, **kwargs):  # order of arguments in function definition
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(args)  # (6, 7, 8)
    print(kwargs)  # {"p": 9, "q": 10}
    return a + b + c + d + e + sum(args) + sum(kwargs.values())


result = addition(1, 2, 3, 4, 5, 6, 7, 8, p=9, q=10)
print(result)


