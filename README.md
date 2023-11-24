# A4_COMP3005
Sameer Ahmadzai
Student Number: 101227616

Youtube Video:


Setup Instructions for database:
1. Create database 'school' by using Pgadmin or using the command:
CREATE DATABASE school;

2. create table with command (using query tool in pgadmin):

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

3. Insert data with command:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


Steps to compile and run your application:
assuming you have python dowloaded:
1. pip install psycopg2
2. run python file in IDE (VSCODE) or in terminal with:
python .\school.py

Function descriptions:
main(): This is the main function that calls other functions to perform operations. It is for organization purposes.
It's structured to demonstrate the addition, retrieval, update, and deletion of student records.

getAllStudents(): This function retrieves all records from the students table. It executes a SELECT * FROM students SQL query 
and fetches all results using cur.fetchall(). Each student record is then printed out, with exception handling for errorss.

addStudent(first_name, last_name, email, enrollment_date): This function adds a new student record to the students table. 
It executes an INSERT INTO SQL statement with the provided student details. There are exception handling for errorss, 
with IntergityError for duplicate student values and general exception handling. 

updateStudentEmail(student_id, new_email): This function updates the email address of a student specified by student_id. 
It executes an UPDATE SQL statement and commits the change, with exception handling for errorss.

deleteStudent(student_id): This function deletes a student record from the students table based on student_id. 
It executes a DELETE SQL statement and commits this change, with exception handling for errorss.
