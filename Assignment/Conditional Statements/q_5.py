# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F)
grade_percen = int(input("Enter Your percentage to display grade: "))

if grade_percen >= 90 :
    grade = 'A'
elif grade_percen >= 80:
    grade = 'B'
elif grade_percen >= 70:
    grade = 'C'
elif grade_percen >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your {grade_percen} percentage and {grade} grade! ")
    

    