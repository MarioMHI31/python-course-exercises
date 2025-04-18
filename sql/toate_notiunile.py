# Libraries
import pymysql

# Connection details (credentials)
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'myfirstdb'

# 1. Make a connection
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    print("Connection successful!")
except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

# 2. Create new database (query <=> stmt)
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS myfirstdb")
    print("Database created successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

# 3. Create new table
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = connection.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """
    cursor.execute(query)
    print("Table created successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

# 4. CRUD (Create, Read, Update, Delete) -> over a Table
# Create
# try:
#     connection = pymysql.connect(
#         host=HOST,
#         port=PORT,
#         user=USER,
#         password=PASSWORD,
#         database=DATABASE
#     )
#
#     cursor = connection.cursor()
#     insert_query = """
#         INSERT INTO student (name, age, grade)
#         VALUES (%s, %s, %s)
#     """
#
#     data = ("Mitarca Sebastian", 27, "A")
#     cursor.execute(insert_query, data)
#     connection.commit() # commit - Create / Insert
#
#     print("Data inserted successfully!")
#
# except pymysql.MySQLError as e:
#     print("Error: ", e)
# finally:
#     connection.close()

# Read
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    select_query = "SELECT * FROM student"
    cursor.execute(select_query)

    results = cursor.fetchall()  # fetchall - Read / Select

    for result in results:
        print(result)

    print("Data inserted successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

# Update
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    update_query = "UPDATE student SET age = %s WHERE name = %s"
    data = (22, "Popescu Mihai")
    cursor.execute(update_query, data)
    connection.commit()

    print("Data updated successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

# Delete
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    delete_query = "DELETE FROM student WHERE name = %s"
    data=("Popescu Mihai",)
    cursor.execute(delete_query, data)
    connection.commit()

    print("Data deleted successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()