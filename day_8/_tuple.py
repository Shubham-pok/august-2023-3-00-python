# Tuple is an immutable datatypes in python
# Tyuple can take diffenet datatypes regardless they are mutable or immutable
#Indexing and slicing in tuple is same as that of list
#tuple elements are enclosed with parenthesis i.e. ()


#creating an empty tuple
t= tuple()
t=()

#creating non-empty tuple
t=(1,1.1,[1,2,3])
print(t) # (1,1.1,[1,2,3])



 ############Accessing Tuple Elements ##################
 #Tuple elements are accessed using indexing and slicing


 vowels = ("a", "e", "i","o","u")
print(vowels[0])
print(vowels[4])
print(vowels[-1])
print(vowels[-3])
#print(vowels[-10])
#print(vowels[20])


data=("a","b","c","d","e","f","g","h","i","j")
print(data[0: 7]) # (,"b","c","d","e","f","g")
print(data[ :5]) #("a","b","c","d","e")
print(data[6: ])#("g","h","i")
print(data[3: 8])#("d","e","f","g","h")
print(data[6: 2])#()
print(data[6: -2])#("g","h")
print(data[-8: -3])#("c","d","e","f","g")
print(data[-9: 8])#("b","c","d","e","f","h")
print(data[-3: -7])#()
print(data[2: 8: 2])#("c","e","g")
print(data[-9: -2: 2])#("b","d","f","h")