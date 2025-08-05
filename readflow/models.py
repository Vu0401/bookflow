from typing import List
import reflex as rx

class Book(rx.Model, table=True):
    title: str
    author: str
    price: float
    cover_url: str
    description: str
    category: str
    rating: float

class Category(rx.Model, table=True):
    name: str
    description: str
