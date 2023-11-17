# app.py
import streamlit as st
import requests

if 'page' not in st.session_state:
    st.session_state.page = 1
      
if 'capitulo' not in st.session_state:
    st.session_state.capitulo = 238

if 'extension' not in st.session_state:
    st.session_state.extension="png"


def render_image():
    st.write(f"Extensão:{st.session_state.extension}" )
    st.write(f"Capitulo {st.session_state.capitulo}")
    st.write(f"Pagina {st.session_state.page}")
    st.image(f"https://img.lermanga.org/J/jujutsu-kaisen/capitulo-{st.session_state.capitulo}/{st.session_state.page}.{st.session_state.extension}")


def add_1_page():
    st.session_state.page +=1
def less_1_page():
    if st.session_state.page>1:
        st.session_state.page -=1

def add_1_cap():
    st.session_state.capitulo +=1
    st.session_state.page =1
def less_1_cap():
    if st.session_state.capitulo>1:
        st.session_state.capitulo -=1
        st.session_state.page=1

def trocar_extension():
    if st.session_state.extension=="png":
        st.session_state.extension= "jpg"
    else:
        st.session_state.extension= "png"


st.button('Trocar para Jpg ou Png', on_click=trocar_extension)

st.button('Voltar Cap', on_click=less_1_cap)
st.button('Proximo Cap', on_click=add_1_cap)


st.button('Voltar imagem', on_click=less_1_page)
st.button('Proxima imagem', on_click=add_1_page)


render_image()

