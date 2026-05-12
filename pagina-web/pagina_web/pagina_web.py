import reflex as rx


def navbar():
    return rx.hstack(
        rx.heading(
            "PedidosGo",
            font_size="2em",
            font_weight="bold",
            color="grey"
        ),
        rx.spacer(),
        rx.hstack(
            rx.button("Iniciar sección", variant="ghost", border_radius="999px", on_click=rx.redirect("https://www.pedidosya.com.do/")),
            rx.button("Registrarse", bg="black", color="white", border_radius="999px", on_click=rx.redirect("https://www.pedidosya.com.do/")),
            spacing="3",
        ),
        width="100%",
        padding="1.5em 3em",
        position="fixed",
        top="0",
        bg="white",
        z_index="100",
    )


def hero():
    return rx.center(
        rx.vstack(
            rx.heading(
                "Pide lo que quieras",
                text_align="center",
                white_space="pre-line",
                font_size=["3em", "5em"],
                line_height="1",
                font_weight="bold",
                color="gray",
            ),
            rx.text(
                "Toda la comida a tu casa\n"
                "Ordena de tus restaurantes favoritos\n",
                text_align="center",
                color="gray",
                white_space="pre-line",
                max_width="600px",
            ),
            rx.button(
                "Ordena ahora",
                bg="black",
                color="white",
                border_radius="999px",
                padding="1.5em 2em",
                on_click=rx.redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", is_external=True),
            ),
            spacing="6",
            align="center",
        ),
        padding_top="10em",
        padding_bottom="3em",
    )


def scooter_section():
    return rx.center(
        rx.image(
            src="https://img.magnific.com/vector-premium/vector-concepto-entrega-alimentos-linea_1162942-1594.jpg?semt=ais_hybrid&w=740&q=80",
            width="700px",
            max_width="90%",
        ),
        padding="2em",
    )



def how_it_works():
    return rx.vstack(
        rx.heading("Cómo funciona", size="8", text_align="center", color= "Gray"),
        rx.text("Pasos simples, estómagos felices.", color="gray", text_align="center"),
        rx.flex(
            step("1", "Elige tu comida", "Explora restaurantes y agrega tus favoritos.", "#f4b400"),
            step("2", "Te la entregamos", "Nuestros repartidores la recogen y entregan rápidamente.", "#00c48c"),
            step("3", "Disfruta tu comida", "Recibe tu pedido y disfruta cada bocado.", "#7b61ff"),
            spacing="8",
            wrap="wrap",
            justify="center",
        ),
        rx.button(
            "Empieza a ordenar",
            bg="black",
            color="white",
            border_radius="999px",
            padding="1.5em 2em",
            on_click=rx.redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
            is_external=True)
        ),
        spacing="7",
        padding="6em 2em",
        align="center",
    )


def step(number, title, text, color):
    return rx.vstack(
        rx.box(
            number,
            bg=color,
            color="white",
            border_radius="999px",
            padding="0.4em 0.8em",
            font_weight="bold",
        ),
        rx.heading(title, size="5"),
        rx.text(text, text_align="center", color="gray", max_width="250px"),
        spacing="3",
        align="center",
    )


def footer():
    return rx.center(
        rx.vstack(
            rx.heading("PedidosGo", font_size="2em"),
            rx.text("Pedido rápido, buena comida.", color="gray"),
            rx.hstack(
                rx.link("Sobre nosotros"),
                rx.link("Privacidad"),
                rx.link("Términos"),
                rx.link("Contacto"),
                spacing="5",
                
            ),
            rx.text("© 2026 PedidosGo", color="gray", font_size="0.9em"),
            spacing="4",
            align="center",
        ),
        padding="4em",
    )
    


def index():
    return rx.center( 
        rx.vstack(
            navbar(),
            hero(),
            scooter_section(),
            how_it_works(),
            footer(),
            spacing="0",
            width="100%",
            max_width="1200px",
            align="center",
        ),
        bg="#f5f5f5",
        position="relative",
        overflow="hidden",
    )


app = rx.App()
app.add_page(index)