# library_management_system (OOPs Concepts)
Project Explanation
Project Structure:
fastapi_project/
main.py: Main application file where the FastAPI app is defined.
models.py: Contains the data models and the Library class to manage the books.
requirements.txt: Lists the dependencies required for the project.
Dependencies:

fastapi: Web framework for building APIs with Python.
uvicorn: ASGI server for running the FastAPI application.
pydantic: Data validation and settings management using Python type annotations.
Files and Their Roles:

models.py:
Defines the Book class using Pydantic for data validation.
Defines the Library class to manage a list of books, with methods to add, get, remove, and list books.
main.py: Sets up the FastAPI application.
Defines endpoints for creating, reading, deleting, and listing books.
requirements.txt: Lists the required packages: fastapi, uvicorn, and pydantic.

Endpoints:
POST /books/: Create a new book.
GET /books/{book_id}: Retrieve a book by its ID.
DELETE /books/{book_id}: Delete a book by its ID.
GET /books/: List all books.
Execution Steps

Set Up the Project Directory:
Create the project directory and navigate into it:
  mkdir fastapi_project
  cd fastapi_project
