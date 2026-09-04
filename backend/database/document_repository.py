from datetime import datetime

from backend.database.db import get_connection
from backend.utils.logger import log_info, log_error


def add_document(filename: str, filepath: str, size: int):
    """
    Add a document to the database.

    Returns:
        int | None: ID of the newly added document.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        upload_time = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO documents
            (filename, filepath, upload_time, size)
            VALUES (?, ?, ?, ?)
        """, (filename, filepath, upload_time, size))

        document_id = cursor.lastrowid

        connection.commit()
        connection.close()

        log_info(f"Document added: {filename}")

        return document_id

    except Exception as error:
        log_error(f"Error adding document '{filename}': {error}")
        return None


def get_document(document_id: int):
    """
    Get a document by its ID.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM documents
            WHERE id = ?
        """, (document_id,))

        document = cursor.fetchone()

        connection.close()

        if document:
            return dict(document)

        return None

    except Exception as error:
        log_error(f"Error retrieving document {document_id}: {error}")
        return None


def get_all_documents():
    """
    Get all documents from the database.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM documents
            ORDER BY upload_time DESC
        """)

        documents = cursor.fetchall()

        connection.close()

        return [dict(document) for document in documents]

    except Exception as error:
        log_error(f"Error retrieving documents: {error}")
        return []


def update_document(document_id: int, filename: str, filepath: str):
    """
    Update document information.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE documents
            SET filename = ?, filepath = ?
            WHERE id = ?
        """, (filename, filepath, document_id))

        connection.commit()

        updated = cursor.rowcount > 0

        connection.close()

        if updated:
            log_info(f"Document updated: {document_id}")

        return updated

    except Exception as error:
        log_error(f"Error updating document {document_id}: {error}")
        return False


def delete_document(document_id: int):
    """
    Delete a document from the database.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM documents
            WHERE id = ?
        """, (document_id,))

        connection.commit()

        deleted = cursor.rowcount > 0

        connection.close()

        if deleted:
            log_info(f"Document deleted: {document_id}")

        return deleted

    except Exception as error:
        log_error(f"Error deleting document {document_id}: {error}")
        return False