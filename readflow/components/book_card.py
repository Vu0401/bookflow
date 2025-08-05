import reflex as rx
from ..models import Book

def book_card(book: Book):
    return rx.card(
        rx.vstack(
            rx.image(
                src=book.cover_url,
                height="400px",
                width="300px",
                object_fit="cover",
                border_radius="var(--radius-3)",
            ),
            rx.vstack(
                rx.heading(book.title, size="4", max_lines=1),
                rx.text(book.author, color_scheme="gray", size="3"),
                rx.hstack(
                    rx.icon(tag="star", color="gold", width="16px", height="16px"),
                    rx.text(f"{book.rating}", size="3"),
                    spacing="1",
                ),
                rx.hstack(
                    rx.text(f"${book.price}", weight="bold", color="green"),
                    rx.button(
                        "Add to Cart",
                        size="2",
                        variant="outline",
                        color_scheme="blue",
                    ),
                    justify="between",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            spacing="3",
            align="center",
        ),
        width="350px",
        padding="3",
        _hover={"box_shadow": "0 4px 6px rgba(0,0,0,0.1)"},
        transition="all 0.2s",
    )
