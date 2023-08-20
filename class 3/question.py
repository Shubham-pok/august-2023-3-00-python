def get_last_item(element ):
    return element[-1]
data= [(4,12,5),(6,1),(11,12),(6,7,8)]
data.sort(key=get_last_item)
print(data)
