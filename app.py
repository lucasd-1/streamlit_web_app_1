import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Web App", page_icon="🐲", layout="wide")
email_contact = "saynomore2@hotmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
css_load("styles/main.css")

url = "https://lottie.host/0f09626a-7287-496e-acbf-3acc4c04c903/YThqNZxRAu.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie=load_lottie(url)


# Intro

with st.container():
    st.header("Hola, somos Web App 👋")
    st.title("Creamos noticias diarias para acompañarte en este proceso")
    st.write("Somos apasionad@s por crear innovación, especializad@s en el sector de digitalización")
    st.write("[Saber más >](https://www.instagram.com/lukeado_)")

# Sobre nosotros

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🛸")
        st.write("""
            Nuestro objetivo es poder ayudarte día a día en la elección de tus ideas, impulsarte a desarrollar todo tu potencial
            creativo:
                 
            - Tenes ideas
            - Tenes ganas
            - Tenes proyectos
            - Queres mejorar
            - Queres ampliar tu vision
            """)
        st.write("Más sobre nosotrxs: https://www.instagram.com/lukeado_")
    with animation_column:
        st_lottie(lottie, height=400)

# Servicios

with st.container():
    st.write("---")
    st.header("Servicios 🛠️")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/apps.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write("""
                Si en tu proceso diario necesitas introducir tus ideas e información o bien tenés que desarrollar tu potencial
                 """)
        st.write("[Ver servicios >] (https://www.instagram.com/lukeado_)")


# Contacto

with st.container():
    st.write("---")
    st.header("Contacta con nosotrxs 📩")
    st.write("##")
    contact_form =f"""
    <form action= "https://formsubmit.co/{email_contact}" method="POST">
        <input type= "text" name="name" placeholder="Tu nombre" required>
        <input type= "email" name="email" placeholder="Tu email" required>
        <input type= "message" name="message" placeholder="Tu mensaje acá" required>
        <button type= "submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
