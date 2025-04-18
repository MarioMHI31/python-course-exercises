from myfirstcon import create_database,create_table,insert_into_table,select_into_table
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'myfirstdb'
if __name__ == '__main__':
    create_database(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)

    #2. call create table

    #Define query
    my_query='''
    CREATE TABLE IF NOT EXISTS my_first_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        );
    '''




    #Call method
    create_table(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE,query=my_query)

   #3. #Call insert into table using a query
    # Define query
    my_insert_query="""
    INSERT INTO my_first_table (first_name, last_name, email)
    VALUES ('Mihai','Mario','mihaimario448@yahoo.com')
    """

    #Call method
    insert_into_table(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE,query=my_insert_query)

    # 4. #Call select into table using a query
    # Define query
    my_select_query = """
        SELECT id,first_name, last_name, email FROM my_first_table
        """

    # Call method
    select_into_table(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, query=my_select_query)