# Import Library
# import mysql.connector
# from mysql.connector import *
# from mysql.connector import connect, Error
#
# # Try to connect (create an object)
# try:
#     with connect(host='sql7.freemysqlhosting.net', port=3306, user='sql7756806', password='vZ1pEImLCX', database='sql7756806') as conn:
#         print(conn)
#         print("Am conexiune!")
#
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT DATABASE();")
#
#         # Example of fetch
#         result = cursor.fetchone()
#         print("Connected to:", result)
#
# except Error as e:
#     print(e)
# finally:
#     print("Nu mai am conexiune!")
#
# # with method() as store_in_something:
# # now we can call store_in_something
#
# '''
# 1. Server
#   2. Database 1
#     3. Table 1
#     3. Table 2
#   2. Database 2
#     3. Table 1
# '''

import pymysql

# Try to connect (create an object)
try:
    with pymysql.connect(host='localhost', port=3306, user='root', password='MDSRMCA12@') as conn:
        print(conn)
        print("Am conexiune!")

        cursor = conn.cursor()

        cursor.execute("SELECT DATABASE();")

        # Example of fetch
        result = cursor.fetchone()
        print("Connected to:", result)

except Error as e:
    print(e)
finally:
    print("Nu mai am conexiune!")