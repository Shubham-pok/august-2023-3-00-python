#We have different method to add and remove items in a set


#add
s={1,2,3}
result=s.add(4)
print(result)#none
print(s)#{1,2,3,4}



#upadte
s.update([4,5,6])
print(s) # {1,2,4,3,6,5}




#discard ()
s.discard(4) # discard () takes elements as an argument
print(s) #{1,2,3,6,5}
s.discard(10) #it doesn't raise error

#remove()
s.remove(5)
print(s) #{1,2,3,6}
s.remove(10) # it raise error

