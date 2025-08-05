import reflex as rx
from ..state import State

def navbar():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.icon(tag="book-open", width="1.5em", height="1.5em"),
                    rx.heading("ReadFlow", size="7"),
                    align="center",
                ),
                href="/",
                _hover={"textDecoration": "none"},
            ),
            rx.spacer(),
            rx.hstack(
                rx.input(
                    placeholder="Search books...",
                    on_change=State.set_search_query,
                    value=State.search_query,
                    width="300px",
                ),
                rx.icon_button(
                    rx.icon(tag="shopping-cart"),
                    variant="outline",
                    size="3",
                ),
                rx.avatar(
                    name="User",
                    size="4",
                ),
                spacing="4",
                align="center",
            ),
            padding_x="4",
            padding_y="3",
            align="center",
            width="100%",
        ),
        bg="white",
        box_shadow="0 2px 10px rgba(0,0,0,0.1)",
        position="sticky",
        top="0",
        z_index="100",
    )
