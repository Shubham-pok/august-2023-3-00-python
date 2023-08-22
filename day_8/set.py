# Set is a mutable datatypes in Python . But,the elements of the set must be immutable
# unlike list ,set is unordered. so , indexing and slicing is not possible in python
#In set to {1,2} is equal to {2,1}
#creating an empty set



#s= set()
#s={} #This is not an empty set. It is and empty dictionary


#creating a non-empty set
#s={1,1.1,(1,2),true 0}
#print(s)


s1= set ([1,2,2,3,1,1,4,2,2])
print(s1) #{1,2,3,4}

#s= {1,[1,2],3} # this is invalid set beacuse it has list as an elements which is mutable
#s= {1,2,(1,2, [3,4])}# this is also invalid because tuple has mutuable elements

