#We can access string elements using indexing and slicing which is similar
# to the list
#forward indexing starts from 0 and reverse indexing from -1


#Indexing
message = "hello world "
print (message[0]) #h
print (message[5]) #<space>
print (message[-1])# d
print(message)#l
#print(message[20]) #error
#print(message[-20]) #error


# slicing
message = "i am learning python "
print(message[:6])#'i am l'
print(message[0:5])#'i am '
print(message[3:8])#'m lea'
print(message[4:])#' learning python'
print(message[7: 2])#''
print(message[-8:-2])#'  pytho'
print(message[-6:-8])#''
print(message[3:-3])#'m learning pyth'
print(message[9:-11])#'n'
print (message[3: 8: 2]) #'mla'

#triple quote string
# creating the object (empty and non-empty )
#accessing the elements (indexing/slicing / accessing elements using key)
#operations
#methods
#Built-in function



#mesage ="Hello"
#message[3]="L"#it is not possible because string is immutable
#print(message)

del message # del is a keyword that is deletes the objects

