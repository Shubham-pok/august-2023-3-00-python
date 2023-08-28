#break ,continue and pass are the special statements in python that can interrupt the flow of the loops
#break and continue are used with loops (for or while) but pass can be used anywhere and not only in loops

for i in range(10):
    if i == 5:
        break
    print(i)

 for i in range(10):
for j in range (i):
     if j == 5;
     break
    print(j)

n = 0
while n <= 10:
    # if n == 5:
    #     break
    print(n)
    n += 1


#continue
#continue statement skips a step in loop
for i in range(10):
    if i == 4:
        continue
    print(i)


n=0
while n<=10:
    if n == 4 :
        n += 1
        continue
    n += 1
    print(n)


#pass
#pass is used to make your code syntatically correct in the places where your logics can be added in future


def addition(a,b):
    pass


#TODO : Need to work in this logic
class student:
    pass




