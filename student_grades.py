students = {
    "Rahul": "A",
    "Priya": "B",
    "Aman": "C"
}

name = input("Enter student name: ")

if name in students:
    print("Student already exists.")
    grade = input("Enter new grade: ")
    students[name] = grade
    print("Grade updated.")
else:
    grade = input("Enter grade: ")
    students[name] = grade
    print("Student added.")

print("\nAll Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)