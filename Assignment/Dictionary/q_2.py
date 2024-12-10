# Iterating through Dictionaries

student = {
    "name" : "umar",
    "age" : 21,
    "grade" : "A"
}

for key in student:
    print(key) 

for value in student.values():
    print(value)


for key, value in student.items():
    print(key," : ",value)


for key in student.keys():
    if key == "grade":
        print(True)
print(False)

count = 0
for key in student.keys():
    count += 1

print(count)



