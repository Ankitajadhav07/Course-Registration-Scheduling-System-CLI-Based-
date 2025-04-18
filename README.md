

**📘 Course Registration & Scheduling System (CLI-Based) | Python + MySQL**
===============================================================================


Author      : Ankita Jadhav  
Created On  : April 2025  
Language    : Python 3.x  
Database    : MySQL (via mysql-connector-python)  

-------------------------------------------------------------------------------
📝 Overview:
-------------------------------------------------------------------------------
This project is a command-line interface (CLI) based Course Registration & 
Scheduling System that allows administrators to manage student information, 
course offerings, and student course registrations using Python and MySQL. 
It demonstrates basic CRUD operations (Create, Read, Update, Delete) and 
efficient use of relational databases with foreign key constraints.

The system simulates a simplified course enrollment platform where:
- Students can be added, viewed, or removed.
- Courses can be added and listed.
- Students can register for courses, and their registration details can be viewed.

-------------------------------------------------------------------------------
💡 Key Features:
-------------------------------------------------------------------------------
✅ Add and view student records  
✅ Add and view course offerings  
✅ Register students to one or more courses  
✅ View courses registered by a particular student  
✅ Remove student records (cascading updates possible if set in DB)  
✅ Clean error handling for MySQL constraints and bad inputs  
✅ Fully interactive CLI-based menu for ease of use  

-------------------------------------------------------------------------------
🗃️ Database Schema:
-------------------------------------------------------------------------------
1. `students`:
    - student_id (Primary Key)
    - name
    - email
    - phone
    - college

2. `courses`:
    - course_id (Primary Key)
    - course_name
    - schedule
    - trainer

3. `registrations`:
    - reg_id (Auto Increment, Primary Key)
    - student_id (Foreign Key)
    - course_id (Foreign Key)
    - registration_date
    - end_date
    - status (e.g., 'active', 'completed')

-------------------------------------------------------------------------------
🔧 Requirements:
-------------------------------------------------------------------------------
- Python 3.x
- MySQL Server
- mysql-connector-python library (`pip install mysql-connector-python`)

-------------------------------------------------------------------------------
🚀 Usage:
-------------------------------------------------------------------------------
1. Ensure MySQL server is running and the `course_system` database is created.
2. Update your MySQL credentials in the script if needed.
3. Run the script: `python course_system.py`
4. Follow the on-screen menu to perform actions.

-------------------------------------------------------------------------------
📈 Future Enhancements (Ideas):
-------------------------------------------------------------------------------
- Add admin login authentication  
- Convert to GUI using Tkinter or PyQt  
- Develop a web-based frontend using Flask/Django  
- Generate reports for registrations and course completion  
- Add course capacity and scheduling conflict logic
-------------------------------------------------------------------------------
🛡️ Disclaimer:
This project is intended for educational/demo purposes and may require 
modification for production-level deployment. Use proper database security 
practices and validation in live systems.


