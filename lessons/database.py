import sqlite3


def create_tables(connection):
    connection.execute('''DROP TABLE IF EXISTS users''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        age INTEGER,
        city TEXT 
    )
    ''')


def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age, city) VALUES 
    (?, ?, ?)
    ''', (student_name, age, city))
    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_tables(conn)

    add_student(conn, "Данил", 18, "Бишкек")
    add_student(conn, "Игорь", 18, "Каракол")