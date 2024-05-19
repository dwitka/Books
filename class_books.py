import sqlite3

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def save_to_db(self, cursor):
        cursor.execute('''
            INSERT INTO books (title, author, year) VALUES (?, ?, ?)
        ''', (self.title, self.author, self.year))

    @staticmethod
    def create_table(cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')

    @staticmethod
    def get_all_books(cursor):
        cursor.execute('SELECT title, author, year FROM books')
        return [Book(row[0], row[1], row[2]) for row in cursor.fetchall()]

    @staticmethod
    def add_book(title, author, year):
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()

        # Create the books table
        Book.create_table(cursor)

        # Create a new book instance
        book = Book(title, author, year)

        # Save the book to the database
        book.save_to_db(cursor)

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()
        return

    @staticmethod
    def print_books():
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()

        # Retrieve all books from the database
        all_books = Book.get_all_books(cursor)

        # Print all books
        for Books in all_books:
            print(Books)

        conn.close()
        return

