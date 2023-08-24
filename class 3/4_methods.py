# copy
a = [1, 2, 3]
b = a
print(a)  # [1,2,3]
print(b)  # [1,2,3]
print(a is b)  # True

b = a.copy()
print(a)  # [1,2,3]
print(b)  # [1,2,3]
print(a is b)  # False. 'a' and 'b' are two diffferent objects

a = [[1, 2, 3], 4]
b = a.copy()
a[0][1] = 7
print(a)  # [[1,7,3],4]
print(b)  # [[1,7,3],4]
# Here 'b' is a shallow copy of 'a' . mutable objects are still the same object in both 'a' and 'b' in Shallow copy


# we can overcome this using deepcopy

from copy import deepcopy

a = [[1, 2, 3], 4]
b= deepcopy(a)
a[0][1] = 7
print(a)  # [[1,7,3],4]
print(b)  ##[[1,2,3],4]
