import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    try:
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        mark = float(input("Enter Mark: "))

        if any(s["id"] == sid for s in students):
            print("ID already exists!")
            return

        students.append({
            "id": sid, "name": name,
            "age": age, "mark": mark
        })
        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Enter valid details!")

def view_students(students):
    if not students:
        print("No student records found!")
        return

    for s in sorted(students, key=lambda x: x["name"]):
        print(s)

def search_student(students):
    try:
        sid = int(input("Enter ID to search: "))
        result = next((s for s in students if s["id"] == sid), None)
        print(result if result else "Student not found!")
    except ValueError:
        print("Invalid ID!")

def update_student(students):
    try:
        sid = int(input("Enter ID to update: "))
        for s in students:
            if s["id"] == sid:
                s["name"] = input("New Name: ")
                s["age"] = int(input("New Age: "))
                s["mark"] = float(input("New Mark: "))
                save_students(students)
                print("Updated successfully!")
                return
        print("Student not found!")
    except ValueError:
        print("Invalid input!")

def delete_student(students):
    try:
        sid = int(input("Enter ID to delete: "))
        remaining = [s for s in students if s["id"] != sid]

        if len(remaining) == len(students):
            print("Student not found!")
        else:
            students[:] = remaining
            save_students(students)
            print("Deleted successfully!")
    except ValueError:
        print("Invalid ID!")

def main():
    students = load_students()

    while True:
        print("\n--- STUDENT RECORD MANAGEMENT ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_student(students)
            elif choice == 2:
                view_students(students)
            elif choice == 3:
                search_student(students)
            elif choice == 4:
                update_student(students)
            elif choice == 5:
                delete_student(students)
            elif choice == 6:
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")

if __name__ == "__main__":
    main()
