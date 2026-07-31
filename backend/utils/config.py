import os

APP_NAME = "Agentic AI Research Assistant"

BASE_DIR = "data"

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

LOG_DIR = os.path.join(BASE_DIR, "logs")

SUPPORTED_EXTENSIONS = [
    ".txt",
    ".pdf",
    ".docx"
]