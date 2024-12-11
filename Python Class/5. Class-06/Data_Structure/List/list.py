# I want to print 100 student name then i make 100 variable name
# studentName1="umar" 
# studentName2="zain" 
# studentName3="hayat" 
# One variable name can store differen value is called list
# studentName=["Umar","Hayat","Zain","naveed","huzifa","umar","umar"]
# How to access item in list
# print(studentName[0])
# output=studentName[0]
# print(output)

# Method of list
# append is no return
# output=studentName.append("ashfaq")
# print(output,"student Name-->",studentName)

# pop can be return
# output=studentName.pop(3)
# print(output,"Student Name",studentName)

# extend is not return and carry argument one as a list name
# studentName1=["ali","john","harry"]
# output=studentName.extend(studentName1)
# print(output,"Student Name",studentName)

# insert is not return and not remove and argument two ,first argu as a index & second argu as a value
# output=studentName.insert(2,"mahad")
# print(output,"student name",studentName)

# index can return & carry arumrnt one as a value
# output=studentName.index(1)
# print(output,"student name",studentName)

# remove is not return & carry one argument as a value & remove first value & value not find then value error 
# output=studentName.remove("umar")
# print(output,"student name",studentName)

# count can be return and take one argument as a value and count the value and if no value find then return 0
# ouput=studentName.count("umar")
# print(ouput,"Student Name: ",studentName)

# sort is not return & no argumrnt & str canot support int & bool  
# studentName=[3,-3,0,1,2,3,4,5,True]     #   [-3, 0, 1, True, 2, 3, 3, 4, 5]   :output
# studentName=[3,-3,0,1,2,3,4,5,False,True]     # [-3, 0, False, 1, True, 2, 3, 3, 4, 5]
# output=studentName.sort(reverse=False)      # same work
# output=studentName.sort(reverse=True)       #   [5, 4, 3, 3, 2, 1, True, 0, -3]
# print(output,"Student Name: ",studentName)


# reverse no return & no argument & 
# studentName=[3,-3,0,1,2,3,4,5,False,True]     #  [True, False, 5, 4, 3, 2, 1, 0, -3, 3]
# output=studentName.reverse()
# print(output,"Student Name: ",studentName)


# clear no return & no argument 
# output=studentName.clear()
# print(output,"Student Name: ",studentName)

#lenght can  return & take one argument as a list name
# output=len(studentName)
# print(output,"Student Name: ",studentName)


studentName=["Umar","Hayat","Zain","naveed","huzifa","umar","umar"]

# Slicing
# output=studentName[1:4]       # note: start index is less than stop index
output=studentName[4:5]    # it is empty
# output=studentName[-5:-2]       
# output=studentName[len(studentName)-5:len(studentName)-2]    it is same   

print(output)





