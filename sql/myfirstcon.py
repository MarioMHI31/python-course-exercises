import pymysql


def create_database(host:str,port:int,user:str,password:str, database:str):
    try:
        #Create my connection object
        my_conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )

        if my_conn:
            print("Successfully connected!", my_conn)


            #with name_of_method as local_name_variables or object
            with my_conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS  {database};")
                print(f"My DB: {database}, has been created or already exists!")



    except pymysql.MySQLError as e:
        print(f"Connection refused: {e}")


def create_table(host:str,port:int,user:str,password:str, database:str,query:str):
    try:
        #Create my connection object
        with pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        ) as my_conn:

            if my_conn:
                print("Successfully connected!", my_conn)

                with my_conn.cursor() as cursor:
                    cursor.execute(query)
                    print("Table has been created!")



    except pymysql.MySQLError as e:
        print(f"Connection refused: {e}")

def insert_into_table(host:str,port:int,user:str,password:str, database:str,query:str):
    try:
        #Create my connection object
        with pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        ) as my_conn:

            if my_conn:
                print("Successfully connected!", my_conn)

                with my_conn.cursor() as cursor:
                    cursor.execute(query)
                    my_conn.commit()




    except pymysql.MySQLError as e:
        print(f"Connection refused: {e}")

def select_into_table(host:str,port:int,user:str,password:str, database:str,query:str):
    try:
        #Create my connection object
        with pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        ) as my_conn:

            if my_conn:
                print("Successfully connected!", my_conn)

                with my_conn.cursor() as cursor:
                    cursor.execute(query)

                    result = cursor.fetchall()
                    for item in result:
                        print(item)




    except pymysql.MySQLError as e:
        print(f"Connection refused: {e}")


