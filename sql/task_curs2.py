from sql.task_curs import create_database,create_table
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'ordering_system'
if __name__ == '__main__':
    create_database(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)


    #2. Create table

    my_query = '''
        CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100) UNIQUE NOT NULL,
                last_name VARCHAR(100) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                age INT NOT NULL,
                adress VARCHAR(255) NOT NULL
            );
        '''



    my_query2 = '''
        CREATE TABLE IF NOT EXISTS `order` (
                id_order INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100) UNIQUE NOT NULL,
                created_at INT NOT NULL,
                coments VARCHAR(255) NOT NULL,
                status VARCHAR(50) NOT NULL
            );
        '''

    create_table(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, query=my_query)

    create_table(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, query=my_query2)