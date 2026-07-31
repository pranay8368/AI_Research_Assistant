from backend.utils.file_manager import (
    save_file,
    load_file,
    delete_file
)

from backend.utils.logger import (
    log_info,
    log_warning,
    log_error
)


def safe_read(filename: str, binary: bool = False):
    """
    Safely read a file.

    Args:
        filename (str): Name of the file.
        binary (bool): True for binary files.

    Returns:
        str | bytes | None:
            File contents if successful, otherwise None.
    """
    try:
        content = load_file(filename, binary)
        log_info(f"Successfully read file: {filename}")
        return content

    except FileNotFoundError:
        log_warning(f"File not found: {filename}")
        return None

    except Exception as error:
        log_error(f"Error reading '{filename}': {error}")
        return None


def safe_write(filename: str, content):
    """
    Safely save a file.

    Args:
        filename (str): Name of the file.
        content (str | bytes): File contents.

    Returns:
        str | None:
            Path of the saved file if successful,
            otherwise None.
    """
    try:
        path = save_file(filename, content)
        log_info(f"Successfully saved file: {filename}")
        return path

    except Exception as error:
        log_error(f"Error saving '{filename}': {error}")
        return None


def safe_delete(filename: str):
    """
    Safely delete a file.

    Args:
        filename (str): Name of the file.

    Returns:
        bool:
            True if deleted successfully,
            False otherwise.
    """
    try:
        if delete_file(filename):
            log_info(f"Successfully deleted file: {filename}")
            return True

        log_warning(f"File not found: {filename}")
        return False

    except Exception as error:
        log_error(f"Error deleting '{filename}': {error}")
        return False


if __name__ == "__main__":
    # Write a file
    path = safe_write("test.txt", "Hello, Agentic AI!")

    if path:
        print(f"Saved at: {path}")

    # Read the file
    content = safe_read("test.txt")
    print("Content:", content)

    # Delete the file
    if safe_delete("test.txt"):
        print("File deleted successfully.")

    # Try reading a deleted file
    print("After deletion:", safe_read("test.txt"))