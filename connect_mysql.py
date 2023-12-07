import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
            host='localhost',
            user='root',
            password='password',
            database=db_name
        )
    except Error as e:
        print(e)

if __name__ == '__main__':
    mydb = connect("pythondb")
    mycursor = mydb.cursor()

    # Create Database
    # mycursor.execute("CREATE DATABASE pythondb")
    
    # Create Table
	#	mycursor.execute("CREATE TABLE EMPLOYEE \
		#   (ID INT PRIMARY KEY NOT NULL,\
		#   NAME TEXT NOT NULL,\
		#   AGE INT NOT NULL,\
		#   ADDRESS CHAR(50),\
		#   SALARY REAL\
		#   );")
        
    # Insert records
	#	mycursor.execute("INSERT INTO pythondb.EMPLOYEE (ID, NAME, AGE, ADDRESS, SALARY)\
		#   VALUES (1, 'Paul', 32, 'paris', 20000.00);\
		#   ")
		
	# mydb.commit()



    # Select from table
    mycursor.execute("SELECT * FROM EMPLOYEE")
    project_records = mycursor.fetchall()
    print(project_records)

    mydb.close()