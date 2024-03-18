import psycopg

# Function to establish a connection to the database
def connect_to_database():
    try:
        #connection info
        conn = psycopg.connect(
            dbname='A3',
            user='postgres',
            password='postgres',
            host='localhost',
            port=5432,
        )
        return conn
    #if error occurs print error
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
        return None

# Function to close the database connection
def close_connection(conn):
    if conn:
        conn.close()

# Function to retrieve all students from the database
def getAllStudents(conn):
    try:
        cursor = conn.cursor()
        script = '''SELECT * FROM students'''
        # Execute the SELECT query to retrieve all students
        cursor.execute(script)  
        # get all the tuples
        rows = cursor.fetchall()
        #print each tuple
        for row in rows:
            print(row)
        print("")
     #if error occurs print error
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Function to add a new student to the database
def addStudent(conn, first_name, last_name, email, enrollment_date):
    try:
        cursor = conn.cursor()
        #query to add new student
        script = '''INSERT INTO students (first_name, last_name, email, enrollment_date) 
                    VALUES (%s, %s, %s, %s);'''
        # Execute INSERT query to add a new student
        cursor.execute(script, (first_name, last_name, email, enrollment_date))  
        conn.commit()
    #if error occurs print error
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Function to update the email of a student in the database
def updateStudentEmail(conn, student_id, new_email):
    try:
        cursor = conn.cursor()
        # Execute UPDATE query to update student email
        cursor.execute('UPDATE students SET email = %s WHERE student_id = %s;', (new_email, student_id))  
        conn.commit()
     #if error occurs print error
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Function to delete a student from the database
def deleteStudent(conn, student_id):
    try:
        cursor = conn.cursor()
        # Execute DELETE query to remove student
        cursor.execute('DELETE FROM students WHERE student_id = %s;', (student_id,))  
        conn.commit()
     #if error occurs print error
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()

# Main program
def main():
    conn = connect_to_database()
    if not conn:
        return
    #code for user interface
    try:
        userinput = -1
        while userinput != 0:
            #all the avaible options
            print("Welcome to Students Database. What would you like to do:")
            print("1. Get all students")
            print("2. Add a new student")
            print("3. Update Student email")
            print("4. Delete a student")
            print("0. Exit")
            #get user input
            userinput = int(input("Please enter your choice: "))
            #if statements to select which function run depending on user input
            if userinput == 1:
                #if 1 get all students
                getAllStudents(conn)
            elif userinput == 2:
                #if 2 get student info 
                first_name = input("First name of student: ")
                last_name = input("Last name of student: ")
                email = input("Email of student: ")
                enrollment_date = input("Enrollment date of student in yyyy-mm-dd format: ")
                # add student
                addStudent(conn, first_name, last_name, email, enrollment_date)
            elif userinput == 3:
                #if 3 get id of student whose email need to be updated
                student_id = input("Enter the ID of the student whose email you want to update: ")
                # get the updated email
                new_email = input("Enter new email: ")
                # update the student email
                updateStudentEmail(conn, student_id, new_email)
            elif userinput == 4:
                # if 4 get student id of student that needs to be removed
                student_id = input("Enter the ID of the student you want to remove: ")
                # delete student
                deleteStudent(conn, student_id)
            elif userinput == 0:
                # if 0 close program
                print("Program closing!")
            else:
                print("Please make a valid selection!\n")
    finally:
        #close the connection
        close_connection(conn)
        

# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()
