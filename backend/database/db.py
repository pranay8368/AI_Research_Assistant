import sqlite3
import os

from backend.utils.config import BASE_DIR
from backend.utils.logger import log_info, log_error


# Database location
DATABASE_PATH = os.path.join(BASE_DIR, "documents.db")


def get_connection():
    """
    Create and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection: Database connection.
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)

        # Allows rows to behave like dictionaries
        connection.row_factory = sqlite3.Row

        return connection

    except sqlite3.Error as error:
        log_error(f"Database connection error: {error}")
        raise


def create_tables():
    """
    Create the required database tables.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                upload_time TEXT NOT NULL,
                size INTEGER NOT NULL
            )
        """)

        connection.commit()
        connection.close()

        log_info("Database tables created successfully.")

    except sqlite3.Error as error:
        log_error(f"Error creating database tables: {error}")
        raise


if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")