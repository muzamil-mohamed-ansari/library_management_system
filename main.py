from fastapi import FastAPI, HTTPException
from models import Book, Library
from typing import List  # Import List from typing


app = FastAPI()
library = Library()

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    if library.get_book(book.id):
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    library.add_book(book)
    return book

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = library.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book

@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    book = library.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    if library.remove_book(book_id):
        return book

@app.get("/books/", response_model=List[Book])
def list_books():
    return library.list_books()
