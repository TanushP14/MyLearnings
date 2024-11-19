import time

name = [
    "Tanush",
    "Udayan",
    "Aman",
    "Araadhya",
    "Aarya",
    "Dakshta",
    "Devansh",
    "Neena Jha",
]

print("Welcome to the School Project Tracker! Let's organize and manage your projects efficiently! Teacher dashboard")
time.sleep(2)

x = str(input("Kindly enter your name for login, My name is "))

print("Searching...")

time.sleep(2)

if x in name:
    print("Login aproved! Please continue your work :)")

else:
    print("Access denied!!  un-authorised person!!")


name = [
    "Tanush",
    "Udayan",
    "Aman",
    "Araadhya",
    "Aarya",
    "Dakshta",
    "Devansh",
    "Neena Jha",
]
project = [
    "Aqua Rover",
    "Eco pulse",
    "Eco pulse ",
    "Smart bin",
    "Smart bin",
    "Eco pulse",
    "Smart bin",
]
status = [
    "Done",
    "Ongoing",
    "Ongoing",
    "Ongoing",
    "Ongoing",
    "Ongoing",
    "Ongoing",
    "Ongoing",
]


x=str(input("What is your agenda to Today, "))

if x == "to get details":
    x=str(input("Enter child's name "))
    if x in name:
        index = name.index(x)  # Get the index of the entered name
        child_name = name[index]
        child_project = project[index]
        child_status = status[index]

        print(f"Details for {child_name}:")
        print(f"Project: {child_project}")
        print(f"Status: {child_status}")
    else:
        print("Child's name not found in the list.")


