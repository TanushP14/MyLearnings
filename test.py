import time
import sys

# Data
students = {
    "Tanush": {"project": "Aqua Rover", "status": "Done"},
    "Udayan": {"project": "Eco Pulse", "status": "Ongoing"},
    "Aman": {"project": "Eco Pulse", "status": "Ongoing"},
    "Araadhya": {"project": "Smart Bin", "status": "Ongoing"},
    "Aarya": {"project": "Smart Bin", "status": "Ongoing"},
    "Dakshta": {"project": "Eco Pulse", "status": "Ongoing"},
    "Devansh": {"project": "Smart Bin", "status": "Ongoing"},
    "Neena Jha": {"project": "Eco Pulse", "status": "Ongoing"},
}

# Welcome Message
print("Welcome to the School Project Tracker! Let's organize and manage your projects efficiently!\n")
time.sleep(2)

# Role Selection
print("Who are you logging in as?")
print("1. Teacher")
print("2. Student")
role = input("\nEnter your role (1 for Teacher, 2 for Student): ").strip()

if role == "1":
    print("\nWelcome, Teacher! Redirecting to your dashboard...\n")
    time.sleep(2)

    # Teacher Menu
    def teacher_dashboard():
        print("\nTeacher Dashboard")
        print("1. Get project details for a student")
        print("2. Update project status")
        print("3. Add a new student")
        print("4. View all student projects")
        print("5. Exit")

    while True:
        teacher_dashboard()
        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            # Get project details
            student_name = input("Enter the student's name: ").strip()
            print("Fetching details...")
            time.sleep(2)

            if student_name in students:
                details = students[student_name]
                print(f"\nDetails for {student_name}:")
                print(f"Project: {details['project']}")
                print(f"Status: {details['status']}")
            else:
                print("Student's name not found in the list.")

        elif choice == 2:
            # Update project status
            student_name = input("Enter the student's name to update: ").strip()
            if student_name in students:
                new_status = input(f"Enter the new status for {student_name} (e.g., Done, Ongoing): ").strip()
                students[student_name]["status"] = new_status
                print(f"Status for {student_name} has been updated to '{new_status}'.")
            else:
                print("Student's name not found in the list.")

        elif choice == 3:
            # Add a new student
            new_name = input("Enter the new student's name: ").strip()
            if new_name in students:
                print(f"{new_name} already exists in the system.")
            else:
                new_project = input(f"Enter the project name for {new_name}: ").strip()
                new_status = input(f"Enter the status for {new_name} (e.g., Done, Ongoing): ").strip()
                students[new_name] = {"project": new_project, "status": new_status}
                print(f"{new_name} has been added to the system with project '{new_project}' and status '{new_status}'.")

        elif choice == 4:
            # View all projects
            print("\nAll Student Projects:")
            for student, details in students.items():
                print(f"{student}: Project - {details['project']}, Status - {details['status']}")

        elif choice == 5:
            # Exit
            print("Exiting the system. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please select a valid option.")

elif role == "2":
    print("\nWelcome, Student! Redirecting to your dashboard...\n")
    time.sleep(2)

    # Student Menu
    def student_dashboard(student_name):
        print(f"\nStudent Dashboard for {student_name}")
        print("1. View my project details")
        print("2. Exit")

    username = input("Please enter your name: ").strip()

    if username in students:
        while True:
            student_dashboard(username)
            try:
                choice = int(input("\nEnter your choice (1-2): "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 2.")
                continue

            if choice == 1:
                # View project details
                details = students[username]
                print(f"\nYour Project Details:")
                print(f"Project: {details['project']}")
                print(f"Status: {details['status']}")

            elif choice == 2:
                # Exit
                print("Logging out. Goodbye!")
                sys.exit()

            else:
                print("Invalid choice! Please select a valid option.")

    else:
        print("Access denied!! Unauthorized person!! :(")
        sys.exit()

else:
    print("Invalid role selection. Please restart the program.")
