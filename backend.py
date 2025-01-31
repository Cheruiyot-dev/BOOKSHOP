from django.db import connection

class BookshopBackend:
    """
    Handles database operations for books and sales.
    """

    # 🔹 Fetch All Books
    @staticmethod
    def get_all_books():
        """
        Fetches all books from the inventory.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, author, price, quantity FROM inventory_book")
            books = cursor.fetchall()
        return books

    # 🔹 Add a New Book
    @staticmethod
    def add_book(title, author, price, quantity):
        """
        Adds a new book to the inventory.
        """
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO inventory_book (title, author, price, quantity) VALUES (%s, %s, %s, %s)",
                [title, author, price, quantity]
            )

    # 🔹 Get a Single Book by ID
    @staticmethod
    def get_book(book_id):
        """
        Fetches a book by its ID.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, author, price, quantity FROM inventory_book WHERE id = %s", [book_id])
            book = cursor.fetchone()
        return book

    # 🔹 Update Book Stock
    @staticmethod
    def update_book_quantity(book_id, quantity):
        """
        Updates the stock quantity of a book.
        """
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE inventory_book SET quantity = %s WHERE id = %s",
                [quantity, book_id]
            )


class SalesBackend:
    """
    Handles book sales processing.
    """

    # 🔹 Record a Sale
    @staticmethod
    def record_sale(book_id, quantity, total_price):
        """
        Records a book sale and updates inventory.
        """
        with connection.cursor() as cursor:
            # Insert sale record
            cursor.execute(
                "INSERT INTO inventory_sales (book_id, quantity_sold, total_price) VALUES (%s, %s, %s)",
                [book_id, quantity, total_price]
            )
            # Reduce stock from inventory
            cursor.execute(
                "UPDATE inventory_book SET quantity = quantity - %s WHERE id = %s",
                [quantity, book_id]
            )

    # 🔹 Get All Sales
    @staticmethod
    def get_sales():
        """
        Fetches all sales records.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, book_id, quantity_sold, total_price FROM inventory_sales")
            sales = cursor.fetchall()
        return sales

    # 🔹 Get Sales for a Specific Book
    @staticmethod
    def get_sales_by_book(book_id):
        """
        Fetches all sales for a specific book.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, quantity_sold, total_price FROM inventory_sales WHERE book_id = %s", [book_id])
            sales = cursor.fetchall()
        return sales
