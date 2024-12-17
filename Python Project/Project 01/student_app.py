# students = []
# def addStudents():
#     studentName = input("Enter Your Name: ")
#     studentAge = int(input("Enter Your Age: "))
#     studentGrade = input("Enter Your Grade: ")
#     students.append({
#         "studentName" : studentName,
#         "studentID" : len(students) + 1,
#         "studentAge" : studentAge,
#         "studentGrade" : studentGrade
#     })

#     print(f"Student {studentName} has successfully added! ")

# def display():
#     if not students:
#         print("Student not found: ")
#     else:
#         print("The Student is: \n")
#         for student in students:
#             print(f"Name : {student['studentName']} ID : {student['studentID']} Age : {student['studentAge']} Grade : {student['studentGrade']} ")

# def searchStudent():
#     studentID = int(input("Search Your ID: "))
#     foundStudent = False
#     for student in students:
#         if student['studentID'] == studentID:
#             print(f"Name : {student['studentName']} ID : {student['studentID']} Age : {student['studentAge']} Grade : {student['studentGrade']} ")
#             foundStudent = True
#     if not foundStudent:
#         print(f"Student ID: {studentID} Not Found ")

# def deleteStudent():
#     studentID = int(input("Type Your ID for Delete: "))
#     for student in students:
#         if student['studentID'] == studentID:
#             students.remove(student)
#             print(f"Student ID: {studentID} has deleted: ")
#             return
#     print(f"Student ID: {studentID} does not exit: ")

# def updateStudent():
#     studentID = int(input("Type your id for update: "))
#     for student in students:
#         if student['studentID'] == studentID:
#             student['studentName'] = input("Enter Your Name: ")
#             student['studentID'] = int(input("Enter Your ID: "))
#             student['studentAge'] = int(input("Enter Your Age: "))
#             student['studentGrade'] = input("Enter Your Grade: ")
#             print(f"Student {studentID} has update: ")
#             return
#     print(f"Student {studentID} does not exit")

# def main():
#     while True:
#         print("\nStudent Management System: ")
#         print("1. Add Student: ")
#         print("2. Display Student: ")
#         print("3. Search Student: ")
#         print("4. Delete Student: ")
#         print("5. Update Student: ")
#         print("6. Exit program: ")
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             addStudents()
#         elif choice == 2:
#             display()
#         elif choice == 3:
#             searchStudent()
#         elif choice == 4:
#             deleteStudent()
#         elif choice == 5:
#             updateStudent()
#         elif choice == 6:
#             print("Exit Program: ")
#             break
#         else:
#             print("invalid input: ")

# if __name__ == "__main__":
#     main()
    
            
class StudentSystemManagement:
    def __init__(self):
        self.students = []
    def addStudents(self):
        id = len(self.students) + 1
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        self.students.append({"id" : id, "name" : name, "age" : age, "grade" : grade})
        print(f"Student : {name} has successfully added")
    def updateStudents(self):
        id = int(input("Type your id for update: "))
        for student in self.students:
            if student['id'] == id:
                student['name'] = input("Update Name: ")
                student['age'] = input("Update Age: ")
                student['grade'] = input("Update Grade: ")
                print(f"Student: {student['name']} has successfully update")
                return
        print(f"Student ID: {id} does not found")
    def readStudents(self):
        if not self.students:
            print(f"Student does not exit: ")
        for student in self.students:
            print(f'Name : {student["name"]} ID : {student["id"]} Grade : {student["grade"]} Age : {student["age"]}')
    def deleteStudents(self):
        id = int(input("Type your id for delete: "))
        for student in self.students:
            if student['id'] == id:
                self.students.remove(student)
                print(f"Student: {student['name']} has deleted been successfully")
                return
        print(f"Student ID: {id} does not found")
    def searchStudents(self):
        id = int(input('Type your id for search: '))
        for student in self.students:
            if student['id'] == id:
                print("Student has found:")
                print(f' Name : {student["name"]} ID : {student["id"]} Grade : {student["grade"]} Age : {student["age"]}')
                return
        print(f"Student ID: {id} does not found")
    def main(self):
        while True:
            print("\nStudent Management System: ")
            print("1. Add Student: ")
            print("2. Update Student: ")
            print("3. Read Student: ")
            print("4. Delete Student: ")
            print("5. Search Student: ")
            print("6. Exit program: ")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.addStudents()
            elif choice == 2:
                self.updateStudents()
            elif choice == 3:
                self.readStudents()
            elif choice == 4:
                self.deleteStudents()
            elif choice == 5:
                self.searchStudents()
            elif choice == 6:
                print("Exit Execution")
                break
if __name__ == '__main__':
    student = StudentSystemManagement()
    student.main()
  

                