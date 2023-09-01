# WAP to create a "login_required" decorator which if added to a function asks for a password. If the
# password is entered "123" then the function can be accessed else throw the message "Invalid Password"


def login_required(func): #func => message
    def inner_func(*args,**kwargs): #txt=> hello world
        password=input("enter your password")
        if password == '123':
            result = func(*args,**kwargs)#message("hello wold")
        else:
            return func(*args,**kwargs)
    return inner_func


@login_required
def addition(a, b):
    return a + b





# WAP to create a "login_required" decorator which if added to a function asks for a password. If the
# password is entered "123" then the function can be accessed else throw the message "Invalid Password"

def login_required(func):
    def inner_func(*args, **kwargs):
        pw = input("Enter your password ")
        if pw == '123':
            return func(*args, **kwargs)
        else:
            return "Invalid Password"
    return inner_func


@login_required
def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)

result = addition(2, 3)
print(result)










def de