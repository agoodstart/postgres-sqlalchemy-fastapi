from classes.postgresdb import Database;

if __name__ == '__main__':
    database = Database()
    database.create_db_connection('EmployeeDB')
    database.engine.connect()

    print(database.engine)