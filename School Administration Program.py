students = {}
def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[id] = {"name": name, "grade": grade}
    print("Student added successfully.")
def view_student():
    id = input("Enter student ID: ")
    if id in students:
        print("ID:", id)
        print("Name:", students[id]["name"])
        print("Grade:", students[id]["grade"])
    else:
        print("Student not found.")
def search_student():
    name = input("Enter student name: ")
    found = False
    for id in students:
        if students[id]["name"] == name:
            print("ID:", id)
            print("Name:", students[id]["name"])
            print("Grade:", students[id]["grade"])
            found = True
    if not found:
        print("Student not found.")
def delete_student():
    id = input("Enter student ID: ")
    if id in students:
        del students[id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
while True:
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")