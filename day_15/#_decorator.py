#Decorators are the function in python which add extra functionality in the existing function
#It is created on the basis of closure function


def extra_message(func):
    def inner_fxn():
        print("I'm learning python")
        return func()
    return inner_fxn


@extra_message
def message():
    print("Hello World ")

#message()
#result=extra_message(message)
#result()
message=extra_message(message)
message()
