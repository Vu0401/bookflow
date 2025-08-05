import reflex as rx
from ..state import State

def category_filter():
    return rx.vstack(
        rx.heading("Categories", size="6"),
        rx.foreach(
            State.categories,
            lambda category: rx.button(
                rx.hstack(
                    rx.text(category.name),
                    rx.badge(
                        "99+", 
                        color_scheme="blue",
                        variant="soft",
                        size="1",
                    ),
                    justify="between",
                    width="100%",
                ),
                on_click=State.set_category(category.name),
                variant="ghost",
                justify="start",
                width="100%",
            ),
        ),
        rx.button(
            "Clear Filters",
            on_click=State.clear_filters,
            variant="outline",
            color_scheme="red",
            size="2",
            margin_top="4",
        ),
        spacing="2",
        align="center",
        width="90%",
    )
