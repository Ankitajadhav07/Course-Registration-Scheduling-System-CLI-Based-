import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql",  
    database="course_system"
)
cursor = conn.cursor()

# === Create Tables ===
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    collage VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    schedule VARCHAR(100),
    trainer VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    registration_date DATE,
    end_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

# === Functions ===
def add_student(student_id, name, email, phone, collage):
    try:
        cursor.execute("INSERT INTO students (student_id, name, email, phone, collage) VALUES (%s, %s, %s, %s, %s)",
                       (student_id, name, email, phone, collage))
        conn.commit()
        print("✅ Student added successfully!")
    except mysql.connector.Error as err:
        print(f" Error: {err}")

def view_students():
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        print(student)

def remove_student(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    print("✅ Student removed!")

def add_course(course_id, course_name, schedule, trainer):
    try:
        cursor.execute("INSERT INTO courses (course_id, course_name, schedule, trainer) VALUES (%s, %s, %s, %s)",
                       (course_id, course_name, schedule, trainer))
        conn.commit()
        print("✅ Course added successfully!")
    except mysql.connector.Error as err:
        print(f" Error: {err}")

def view_courses():
    cursor.execute("SELECT * FROM courses")
    for course in cursor.fetchall():
        print(course)

def register_course(student_id, course_id, registration_date, end_date, status):
    try:
        cursor.execute("""
        INSERT INTO registrations (student_id, course_id, registration_date, end_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """, (student_id, course_id, registration_date, end_date, status))
        conn.commit()
        print("✅ Registration successful!")
    except mysql.connector.Error as err:
        print(f" Error: {err}")

def view_student_courses(student_id):
    cursor.execute("""
        SELECT c.course_name, c.schedule, c.trainer, r.registration_date, r.end_date, r.status
        FROM courses c
        JOIN registrations r ON c.course_id = r.course_id
        WHERE r.student_id = %s
    """, (student_id,))
    results = cursor.fetchall()
    if not results:
        print("⚠️ No registered courses.")
    else:
        for course in results:
            print(f"""
Course: {course[0]}
Schedule: {course[1]}
Trainer: {course[2]}
Registered On: {course[3]}
Ends On: {course[4]}
Status: {course[5]}
-----------------------------""")

# === Menu ===
while True:
    print("""
\n=== Course Registration & Scheduling System ===
1. Add Student
2. View Students
3. Add Course
4. View Courses
5. Register Student to Course
6. View Student Registrations
7. Exit
8. Remove Student
""")
    choice = input("Enter choice: ")

    if choice == '1':
        sid = int(input("Student ID: "))
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        collage = input("Collage Name: ")
        add_student(sid, name, email, phone, collage)

    elif choice == '2':
        view_students()

    elif choice == '3':
        cid = int(input("Course ID: "))
        cname = input("Course Name: ")
        schedule = input("Schedule (e.g., Mon-Wed 10AM): ")
        trainer = input("Trainer Name: ")
        add_course(cid, cname, schedule, trainer)

    elif choice == '4':
        view_courses()

    elif choice == '5':
        sid = int(input("Student ID: "))
        cid = int(input("Course ID: "))
        reg_date = input("Registration Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        status = input("Status (e.g., active/completed): ")
        register_course(sid, cid, reg_date, end_date, status)

    elif choice == '6':
        sid = int(input("Enter Student ID to view courses: "))
        view_student_courses(sid)

    elif choice == '7':
        print("Exiting... ✅")
        break
    elif choice == '8':
        sid = int(input("Student ID to remove: "))
        remove_student(sid)

    else:
        print(" Invalid choice! Try again.")

