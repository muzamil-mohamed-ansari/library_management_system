from typing import List, Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_book(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def remove_book(self, book_id: int) -> bool:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def list_books(self) -> List[Book]:
        return self.books
