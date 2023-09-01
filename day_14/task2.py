#Create a new list of repeated items from a provided list:
#nums = [3, 4, 2, 2, 1, 3, 3, 3]
#Output = [3, 2]

nums = [3,4,2,2,1,3,3,3]
output = []
for i in nums:
    if nums.count(i)>1 an i not in output:
        output.append(i)

print(output)