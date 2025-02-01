##
## Armando Gomez
## CSC500-1   Principals of Programming
## Module 7: Critical Thinking Assignment
## Doctor Jessica Schwartz


# Step 0: Let's print School Course Schedule
print("\n📚 PUGwarts School of Wizardry Course Schedule\n")

#

# Step 1: Creation and storage of course details in dictionaries
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
    "MAJ101": "1212"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
    "MAJ101": "Snape"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
    "MAJ101": "12:00 a.m."
}

# Step 2: Ask the user to enter a course number
course_number = input("Enter a course number (e.g., CSC101): ").strip().upper()

# Step 3: program checks if course with course number is in the system
if course_number in course_rooms:
    print("\n📚 Course Details:")
    print(f"🏢 Room Number: {course_rooms[course_number]}")
    print(f"👨‍🏫 Instructor: {course_instructors[course_number]}")
    print(f"⏰ Meeting Time: {course_times[course_number]}")

# if course isn't in system display error message    
else:
    print("❌ Error: Course not found. Double-check the course number and try again!")
