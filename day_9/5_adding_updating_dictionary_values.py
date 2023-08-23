student= {"name":"jane","age": 30,"address":"ktm"}
student ["roll_no"]= 21
print(student) #student= {"name":"jane","age": 30,"address":"ktm","roll_no":21}

student["name"] = "jon"
print(student) #student= {"name":"jone","age": 30,"address":"ktm","roll_no"=21}

other_info={"institute":"Broadway","phone_no":9890989878}
student.update(other_info)
print(student) ##student= {"name":"jone","age": 30,"address":"ktm","roll_no"=21,"institute":"Broadway","phone_no"=9890989878}


student.update(last_name="ABC")
print(student)


