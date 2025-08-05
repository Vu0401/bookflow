import reflex as rx
from typing import List
from .models import Book, Category

class State(rx.State):
    books: List[Book] = []
    categories: List[Category] = []
    selected_category: str = ""
    search_query: str = ""
    
    def load_data(self):
        # Mock data
        self.categories = [
            Category(name="Fiction", description="Fictional stories"),
            Category(name="Non-Fiction", description="Real world stories"),
            Category(name="Science Fiction", description="Sci-fi adventures"),
            Category(name="Mystery", description="Thrilling mysteries"),
            Category(name="Romance", description="Love stories"),
        ]
        
        self.books = [
            Book(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                price=12.99,
                cover_url="https://placehold.co/300x450/4f46e5/white?text=The+Great+Gatsby",
                description="A classic American novel set in the Jazz Age.",
                category="Fiction",
                rating=4.5
            ),
            Book(
                title="To Kill a Mockingbird",
                author="Harper Lee",
                price=14.99,
                cover_url="https://placehold.co/300x450/ec4899/white?text=To+Kill+a+Mockingbird",
                description="A gripping tale of racial injustice and childhood innocence.",
                category="Fiction",
                rating=4.8
            ),
            Book(
                title="1984",
                author="George Orwell",
                price=13.99,
                cover_url="https://placehold.co/300x450/0ea5e9/white?text=1984",
                description="A dystopian social science fiction novel.",
                category="Science Fiction",
                rating=4.7
            ),
            Book(
                title="Pride and Prejudice",
                author="Jane Austen",
                price=11.99,
                cover_url="https://placehold.co/300x450/10b981/white?text=Pride+and+Prejudice",
                description="A romantic novel of manners set in Georgian society.",
                category="Romance",
                rating=4.6
            ),
            Book(
                title="The Catcher in the Rye",
                author="J.D. Salinger",
                price=13.49,
                cover_url="https://placehold.co/300x450/f59e0b/white?text=The+Catcher+in+the+Rye",
                description="A controversial novel about teenage rebellion.",
                category="Fiction",
                rating=4.2
            ),
            Book(
                title="Dune",
                author="Frank Herbert",
                price=16.99,
                cover_url="https://placehold.co/300x450/ef4444/white?text=Dune",
                description="An epic science fiction novel set in the distant future.",
                category="Science Fiction",
                rating=4.9
            ),
        ]
    
    def filter_books(self):
        if not self.selected_category and not self.search_query:
            return self.books
        
        filtered = self.books
        if self.selected_category:
            filtered = [book for book in filtered if book.category == self.selected_category]
        
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                book for book in filtered 
                if query in book.title.lower() or query in book.author.lower()
            ]
        
        return filtered

    def set_category(self, category: str):
        self.selected_category = category

    def set_search_query(self, query: str):
        self.search_query = query

    def clear_filters(self):
        self.selected_category = ""
        self.search_query = ""
    
    @rx.var
    def filtered_books_count(self) -> int:
        return len(self.filter_books())
    
    @rx.var 
    def books_count(self) -> int:
        return len(self.books)
