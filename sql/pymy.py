import pymysql

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'myfirstdb'

#conn, connection, my_conn
#Make connection

connection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
print(f"Successfully connected!({connection})")

def bulk_insert(connection,elements):
    if not elements:
        return

    insert_query = """
    INSERT INTO my_first_table (first_name, last_name, email)
    VALUES (%s, %s, %s)
    """

    connection.cursor().executemany(insert_query, elements)
    connection.commit()
if __name__ == '__main__':
    elements = [
        ('Nume1','Prenume1','email1@gmail.com'),
        ('Nume2','Prenume2','email2@gmail.com'),
        ('Nume3','Prenume3','email3@gmail.com'),
    ]

    #Context Manager
    with connection:
        bulk_insert(connection,elements)