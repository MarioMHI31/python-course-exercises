import pymysql

#
# connection = pymysql.connect(host='localhost',port=3306,user='root',password='MDSRMCA12@',database='ordering_system')
# print(f"Successfully connected!({connection})")
#
# def create_database(host:str, port:int,  user:str, password:str, database:str):
#     try:
#         my_conn=pymysql.connect(
#             host=host,
#             port=port,
#             user=user,
#             password=password
#         )
#
#         if my_conn:
#             print("Successfully connected!",my_conn)
#
#             with my_conn.cursor() as cursor:
#                 cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
#                 print(f"My DB: {database}, has been created or already exists!")
#
#     except pymysql.MySQLError as e:
#         print(f"Connection refused: {e}")
#
# def create_table(host:str, port:int,  user:str, password:str, database:str,query:str):
#     try:
#         with pymysql.connect(
#             host=host,
#             port=port,
#             user=user,
#             password=password,
#             database=database
#         ) as my_conn:
#
#             if my_conn:
#                 print("Successfully connected!", my_conn)
#
#                 with my_conn.cursor() as cursor:
#                     cursor.execute(query)
#                     print("Table has been created!")
#
#     except pymysql.MySQLError as e:
#         print(f"Connection refused: {e}")
#



# def bulk_insert(connection, elements):
#     if not elements:
#         return
#
#     insert_query = """
#     INSERT INTO user (first_name, last_name, email, age, address)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#
#
#     with connection.cursor() as cursor:
#         cursor.executemany(insert_query, elements)
#         connection.commit()
#         print(f"{cursor.rowcount} users inserted successfully.")
#
# elements = [
#     ('Ion', 'Popescu', 'ion.popescu@example.com', 28, 'Strada Mihai Eminescu, București'),
#     ('Maria', 'Ionescu', 'maria.ionescu@example.com', 34, 'Bdul Unirii, Cluj-Napoca'),
#     ('Alexandru', 'Vasilescu', 'alexandru.vasilescu@example.com', 40, 'Strada Moșilor, Iași'),
#     ('Elena', 'Petrescu', 'elena.petrescu@example.com', 25, 'Strada Lunga, Timișoara'),
#     ('Andrei', 'Dumitru', 'andrei.dumitru@example.com', 30, 'Calea Victoriei, Brașov'),
#     ('Ioana', 'Popa', 'ioana.popa@example.com', 22, 'Strada Al. I. Cuza, Constanța'),
#     ('Radu', 'Constantin', 'radu.constantin@example.com', 27, 'Strada Timiș, Craiova'),
#     ('Gabriela', 'Stan', 'gabriela.stan@example.com', 29, 'Strada Vasile Alecsandri, Ploiești'),
#     ('Mihai', 'Nistor', 'mihai.nistor@example.com', 35, 'Bdul Ion Mihalache, Sibiu'),
#     ('Larisa', 'Marin', 'larisa.marin@example.com', 33, 'Strada Republicii, Arad')
# ]
#
#
#
# with connection:
#     bulk_insert(connection, elements)



# Task:
# Sa creem o baza de date: "shoppinglists"
# Sa creem un tabel: "my_list" (id, item, price, comments)
# Sa aplicam operatiile CRUD asupra tabelului
# ! Sa fie secure (SQLInjection)

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'shoppinglists'

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD
    )
    print("Connection successful!")
except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS shoppinglists")
    print("Database created successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = connection.cursor()
    query="""
    CREATE TABLE IF NOT EXISTS my_list(
        id INT AUTO_INCREMENT PRIMARY KEY,
        item VARCHAR(100) NOT NULL,
        price INT NOT NULL,
        comments VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(query)
    print("Table created successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

#Create
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    insert_query = """
        INSERT INTO my_list (item,price,comments)
        VALUES (%s, %s, %s)
    """

    data = ("Televizor samsung", 4000, "Cel mai calitativ ecran dupa piata.")
    cursor.execute(insert_query, data)
    connection.commit()

    print("Data inserted successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

#Read

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    select_query= """
    SELECT * FROM my_list
    """
    cursor.execute(select_query)

    results = cursor.fetchall()
    for result in results:
        print(result)
except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

#update
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    update_query="""
    Update my_list SET price = %s WHERE item = %s
    """
    data=(2000,"televizor samsung")
    cursor.execute(update_query, data)
    connection.commit()

    print("Data updated successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()

#delete
try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = connection.cursor()
    delete_query="""
    DELETE FROM my_list WHERE item = %s
    """
    data=("televizor samsung",)
    cursor.execute(delete_query, data)
    connection.commit()

    print("Data deleted successfully!")

except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    connection.close()
