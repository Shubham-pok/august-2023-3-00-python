data = [(10,12),(3,5),(2,1),(40,10),(93,8)]
#result [(2,1). (3,5) (3,8) (40,10)(10,12)]

def get_second_element(element ):
    return element[1]

data.sort(key=get_second_element)
print(data)
