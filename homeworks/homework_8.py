import sqlite3

def create_table(connection):
    connection.execute("DROP TABLE IF EXISTS books")
    connection.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    connection.commit()


def insert_books(connection):
    books = [
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 5),
        ("Мастер и Маргарита", "М. Булгаков", 1967, "Роман", 470, 12),
        ("Преступление и наказание", "Ф. Достоевский", 1866, "Роман", 430, 4),
        ("Гарри Поттер", "Дж. Роулинг", 1997, "Фэнтези", 223, 7),
        ("Война и мир", "Л. Толстой", 1869, "Роман", 1225, 6),
        ("Анна Каренина", "Л. Толстой", 1877, "Роман", 864, 8),
        ("Маленький принц", "А. де Сент-Экзюпери", 1943, "Сказка", 96, 10),
        ("451 градус по Фаренгейту", "Р. Брэдбери", 1953, "Антиутопия", 256, 3),
        ("Шерлок Холмс", "А. Конан Дойл", 1892, "Детектив", 307, 10),
        ("Над пропастью во ржи", "Д. Сэлинджер", 1951, "Роман", 277, 5)
    ]

    connection.executemany("""
        INSERT INTO books (
            name, author, publication_year, genre,
            number_of_pages, number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()

def delete_book(connection, book_id):
    connection.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    connection.commit()


def change_book(connection, book_id, new_name, new_author,
                new_pub_year, new_genre, new_number_of_pages, new_number_of_copies):
    connection.execute("""
        UPDATE books
        SET name = ?, author = ?, publication_year = ?, genre = ?,
            number_of_pages = ?, number_of_copies = ?
        WHERE id = ?
    """, (
        new_name, new_author, new_pub_year, new_genre,
        new_number_of_pages, new_number_of_copies, book_id
    ))
    connection.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("homework_8.db")
    create_table(conn)
    insert_books(conn)


    delete_book(conn, 1)
    change_book(conn, 2, "Собачье сердце", "М. Булгаков",
                1968, "Антиутопия", 12,
                3 )

    conn.close()