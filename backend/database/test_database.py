from backend.database.db import create_tables

from backend.database.document_repository import (
    add_document,
    get_document,
    get_all_documents,
    update_document,
    delete_document
)


# Create database table
create_tables()


# Add documents
id1 = add_document(
    "research_paper.pdf",
    "data/uploads/research_paper.pdf",
    250000
)

id2 = add_document(
    "machine_learning.pdf",
    "data/uploads/machine_learning.pdf",
    500000
)

print("\nAdded IDs:")
print(id1)
print(id2)


# Get one document
print("\nOne document:")
print(get_document(id1))


# Get all documents
print("\nAll documents:")

for document in get_all_documents():
    print(document)


# Update
print("\nUpdating document:")

print(
    update_document(
        id1,
        "updated_research_paper.pdf",
        "data/uploads/updated_research_paper.pdf"
    )
)


# Get updated document
print("\nUpdated document:")
print(get_document(id1))


# Delete
print("\nDeleting document:")

print(delete_document(id2))


# Final documents
print("\nFinal documents:")

for document in get_all_documents():
    print(document)