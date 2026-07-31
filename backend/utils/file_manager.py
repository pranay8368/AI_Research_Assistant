import os
from backend.utils.config import UPLOAD_DIR


# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_file(filename: str, content) -> str:
    """
    Save a file to the uploads directory.

    Args:
        filename (str): Name of the file.
        content (str or bytes): File content.

    Returns:
        str: Full path of the saved file.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    mode = "wb" if isinstance(content, bytes) else "w"

    with open(file_path, mode, encoding=None if mode == "wb" else "utf-8") as file:
        file.write(content)

    return file_path


def load_file(filename: str, binary: bool = False):
    """
    Load a file from the uploads directory.

    Args:
        filename (str): Name of the file.
        binary (bool): True for binary files like PDFs.

    Returns:
        str or bytes: File contents.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{filename}' not found.")

    mode = "rb" if binary else "r"

    with open(file_path, mode, encoding=None if binary else "utf-8") as file:
        return file.read()


def delete_file(filename: str) -> bool:
    """
    Delete a file from the uploads directory.

    Args:
        filename (str): Name of the file.

    Returns:
        bool: True if deleted, False otherwise.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        return True

    return False


def list_files() -> list:
    """
    List all files in the uploads directory.

    Returns:
        list: List of filenames.
    """
    return [
        file
        for file in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, file))
    ]


if __name__ == "__main__":
    save_file("test.txt", "Hello, Agentic AI!")
    print(load_file("test.txt"))
    print(list_files())
    delete_file("test.txt")