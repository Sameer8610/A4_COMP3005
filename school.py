import psycopg2
from psycopg2 import IntegrityError

# Connect to postgres Database
# Connection parameters: dbname, user, password, host
connection = psycopg2.connect("dbname=school user=postgres password=admin host=localhost")

# Open a cursor to perform database operations
cur = connection.cursor()

# Function to get and display all students from the 'students' table
def getAllStudents():
    try:
        # Execute SQL query to select all records from the 'students' table
        cur.execute("SELECT * FROM students;")
        students = cur.fetchall() # Fetch all the results of the query
        for student in students:
            print(student) # Print each student's details
            
    # Print any exception that occurs     
    except Exception as e:
        print(f"Error in getAllStudents: {e}")

# Function to add a new student to the 'students' table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        # Execute SQL query to insert a new student record into the 'students' table
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", 
                    (first_name, last_name, email, enrollment_date))
        connection.commit() # Commit the transaction
    
     # Handle unique constraint violation  
    except IntegrityError:
        print(f"Error: A student with the email {email} already exists.")
    
    # Print any other exception that occurs  
    except Exception as e:
        print(f"Error in addStudent: {e}")

# Function to update a student's email in the 'students' table
def updateStudentEmail(student_id, new_email):
    try:
        # Execute SQL query to update email of a student based on student_id
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
        connection.commit() # Commit the transaction
    
    # Print any exception that occurs 
    except Exception as e:
        print(f"Error in updateStudentEmail: {e}")

# Function to delete a student from the 'students' table
def deleteStudent(student_id):
    try:
        # Execute SQL query to delete a student based on student_id
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        connection.commit() # Commit the transaction
      
    # Print any exception that occurs  
    except Exception as e:
        print(f"Error in deleteStudent: {e}")

#main function with function calls
def main():
    getAllStudents()

#call main
if __name__ == "__main__":
    main()
    
# Close the cursor and connection to the database
cur.close()
connection.close()
