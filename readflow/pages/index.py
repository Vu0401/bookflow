import reflex as rx
from ..components.navbar import navbar
from ..components.book_card import book_card
from ..components.category_filter import category_filter
from ..state import State

# Main page - load data when page loads
@rx.page(on_load=State.load_data)
def index():
    return rx.box(
        navbar(),  # Top navbar

        rx.container(
            rx.hstack(
                # --- Sidebar ---
                rx.box(
                    category_filter(),
                    width="300px",
                    padding_right="3",
                    border_right="1px solid var(--gray-6)",
                ),

                # --- Main Content ---
                rx.box(
                    rx.vstack(
                        # Heading + Book count
                        rx.hstack(
                            rx.heading("Featured Books", size="7"),
                            rx.badge(
                                f"{State.books_count} books",
                                color_scheme="blue",
                                size="2",
                            ),
                            justify="between",
                            width="280%",
                        ),

                        rx.separator(),  # Divider

                        # Selected Category (if any)
                        rx.cond(
                            State.selected_category,
                            rx.text(
                                f"Category: {State.selected_category}",
                                color_scheme="gray",
                                size="3",
                            ),
                        ),

                        # Search Query (if any)
                        rx.cond(
                            State.search_query,
                            rx.text(
                                f"Search results for: {State.search_query}",
                                color_scheme="gray",
                                size="3",
                            ),
                        ),

                        # Book Grid
                        rx.grid(
                            rx.foreach(State.books, book_card),
                            columns="repeat(auto-fill, minmax(300px, 1fr))",
                            spacing="9",
                            width="280%",
                        ),

                        spacing="5",
                        width="100%",
                    ),
                    width="60%",
                ),

                spacing="6",
                width="100%",
            ),
            padding_y="3",
            max_width="900px",
        ),

        min_height="300vh",
        background="var(--gray-2)",
    )
