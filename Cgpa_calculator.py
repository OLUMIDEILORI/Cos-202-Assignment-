print("=" * 50)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 50)

num_courses = int(input("Enter number of courses: "))

total_units = 0
total_grade_points = 0

for i in range(num_courses):
    print("\nCourse", i + 1)

    course = input("Course Title: ")

    unit = int(input("Course Unit: "))

    grade = input("Grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    elif grade == "F":
        point = 0
    else:
        print("Invalid grade entered.")
        point = 0

    total_units += unit
    total_grade_points += unit * point

cgpa = total_grade_points / total_units

print("\n")
print("=" * 50)
print("RESULT")
print("=" * 50)
print("Total Units:", total_units)
print("Total Grade Points:", total_grade_points)
print("CGPA: {:.2f}".format(cgpa))

if cgpa >= 4.50:
    classification = "FIRST CLASS"
elif cgpa >= 3.50:
    classification = "SECOND CLASS UPPER"
elif cgpa >= 2.40:
    classification = "SECOND CLASS LOWER"
elif cgpa >= 1.50:
    classification = "THIRD CLASS"
elif cgpa >= 1.00:
    classification = "PASS"
else:
    classification = "FAIL"

print("Class of Degree:", classification)

print("=" * 50)
print("Thank you for using Personal Pocket CGPA Calculator")