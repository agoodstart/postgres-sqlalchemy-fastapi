from classes.postgresdb import Database;

if __name__ == '__main__':
    database = Database()
    database.create_db_connection('EmployeeDB')
    conn = database.engine.connect()

    data = conn.execute('SELECT * FROM tblEmployee;')
    print(data.fetchall())