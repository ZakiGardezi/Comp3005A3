import psycopg

def getAllStudents():
    try :
        conn = psycopg.connect (
        dbname='A3',
        user='postgres',
        password='postgres',
        host='localhost',
        port= 5432,
        )

        cursor  = conn.cursor() 

        script = '''Select * 
                    From students'''
        
        cursor.execute(script)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("")

        cursor.close()
        conn.close()
    except psycopg.OperationalError as e:
        print(f"Error:{e}" ) 


def addStudent(first_name, last_name, email, enrollment_date):
    try :
        conn = psycopg.connect (
        dbname='A3',
        user='postgres',
        password='postgres',
        host='localhost',
        port= 5432,
        )

        cursor  = conn.cursor() 

        # Using parameterized query to insert values
        script = '''INSERT INTO students (first_name, last_name, email, enrollment_date) 
                    VALUES (%s, %s, %s, %s);'''
        
        # Execute the query with the values passed as parameters
        cursor.execute(script, (first_name, last_name, email, enrollment_date))
        conn.commit()

        cursor.close()
        conn.close()
    except psycopg.OperationalError as e:
        print(f"Error:{e}" ) 

def updateStudentEmail(student_id , new_email):
    try :
        conn = psycopg.connect (
        dbname='A3',
        user='postgres',
        password='postgres',
        host='localhost',
        port= 5432,
        )

        cursor  = conn.cursor() 
        cursor.execute('UPDATE students SET email = %s WHERE student_id = %s;', (new_email, student_id))
        conn.commit()

        cursor.close()
        conn.close()
    except psycopg.OperationalError as e:
        print(f"Error:{e}" ) 

def deleteStudent(student_id):
    try :
        conn = psycopg.connect (
        dbname='A3',
        user='postgres',
        password='postgres',
        host='localhost',
        port= 5432,
        )

        cursor  = conn.cursor() 
        cursor.execute('DELETE FROM students WHERE student_id = %s;', (student_id,))
        conn.commit()

        cursor.close()
        conn.close()
    except psycopg.OperationalError as e:
        print(f"Error:{e}" ) 

#main program
userinput = -1
while userinput != 0:
    print("Welcome to Students Database. What would you like to do:")
    print("1. Get all students")
    print("2. Add a new student")
    print("3. Update Student email")
    print("4. Delete a student")
    print("0. Exit")
    userinput = int(input("Please enter your choice: "))
    if userinput == 1:
        getAllStudents()
    elif userinput == 2:
        first_name = input("First name of student: ")
        last_name = input("Last name of student: ")
        email = input("Email of student: ")
        enrollment_date = input("Enrollement date of student in yyyy-mm-dd format: ")
        addStudent(first_name, last_name, email, enrollment_date)
    elif userinput == 3:
        student_id = input("Enter the ID of the student whose email you want to update: ")
        new_email = input("Enter new email: ")
        updateStudentEmail(student_id, new_email)
    elif userinput == 4:
        student_id = input("Enter the ID of the student you want to remove: ")
        deleteStudent(student_id)
    else:
        print("Please make a valid selection!\n")

print("Program closing!")