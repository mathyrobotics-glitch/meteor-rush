import streamlit as st

st.set_page_config(
    page_title="Meteor Rush",
    page_icon="☄️",
    layout="wide"
)

st.title("☄️ METEOR RUSH")
st.subheader("¡Sobrevive a la lluvia de meteoritos!")

st.write("""
Meteor Rush es un videojuego arcade desarrollado en Python
para micro:bit. El jugador controla una nave espacial y
debe esquivar meteoritos para conseguir puntos.
""")

st.divider()

st.header("🎮 Reglas y controles")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Controles")
    st.write("⬅️ Botón A: mover a la izquierda")
    st.write("➡️ Botón B: mover a la derecha")

with col2:
    st.subheader("Reglas")
    st.write("☄️ Esquivar los meteoritos")
    st.write("⭐ Cada meteorito esquivado suma un punto")
    st.write("💥 Si hay una colisión, termina el juego")

st.divider()

st.header("🚀 Explora Meteor Rush")

opcion = st.selectbox(
    "Selecciona una sección:",
    ["Historia", "Objetivo", "Funcionamiento"]
)

if opcion == "Historia":
    st.write("Una nave espacial intenta sobrevivir a una peligrosa lluvia de meteoritos.")

elif opcion == "Objetivo":
    st.write("Conseguir la mayor puntuación posible sin chocar.")

else:
    st.write("El juego utiliza los botones A y B, variables, funciones, condicionales y ciclos.")

st.divider()

st.header("📊 Diagrama de flujo")

st.graphviz_chart("""
digraph {
    Inicio -> Crear_nave
    Crear_nave -> Caida_meteorito
    Caida_meteorito -> Colision
    Colision -> Fin [label="Sí"]
    Colision -> Sumar_punto [label="No"]
    Sumar_punto -> Nuevo_meteorito
    Nuevo_meteorito -> Caida_meteorito
}
""")

st.divider()

st.header("💻 Código del videojuego")

with st.expander("Ver código"):
    st.code("""
nave = game.create_sprite(2, 4)
meteorito = game.create_sprite(randint(0, 4), 0)
velocidad = 500

def nuevo_meteorito():
    meteorito.set(LedSpriteProperty.X, randint(0, 4))
    meteorito.set(LedSpriteProperty.Y, 0)

def mover_izquierda():
    if nave.get(LedSpriteProperty.X) > 0:
        nave.move(-1)

input.on_button_pressed(Button.A, mover_izquierda)

def mover_derecha():
    if nave.get(LedSpriteProperty.X) < 4:
        nave.move(1)

input.on_button_pressed(Button.B, mover_derecha)

def jugar():
    global velocidad
    basic.pause(velocidad)
    meteorito.change(LedSpriteProperty.Y, 1)

    if meteorito.is_touching(nave):
        game.game_over()
    elif meteorito.get(LedSpriteProperty.Y) == 4:
        game.add_score(1)
        nuevo_meteorito()

        if velocidad > 180:
            velocidad -= 20

basic.forever(jugar)
""", language="python")

st.divider()

st.header("👤 Integrante")

st.write("Matito Storm")
st.write("Diseño, programación y desarrollo del proyecto.")

st.caption("Universidad Sergio Arboleda | Diseño Digital | 2026")
