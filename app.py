# app.py
import streamlit as st
from io import BytesIO
import requests



if 'page' not in st.session_state:
    st.session_state.page = 1
    st.session_state.start_page = ""

if 'capitulo' not in st.session_state:
    st.session_state.capitulo = 1
    st.session_state.capitulo_antigo = 1

if 'extension' not in st.session_state:
    st.session_state.extension="png"

if "manga" not in st.session_state:
    st.session_state.manga = "None"
    st.session_state.manga_antigo = "None"



st.session_state.manga =st.selectbox("Qual manga vai ler?",("None","Boku no Hero","Jujutsu Kaisen"))
if st.session_state.manga != st.session_state.manga_antigo :
    st.session_state.page = 1
    st.session_state.manga_antigo  = st.session_state.manga

if st.session_state.manga == "Boku no Hero":
    url_base = "https://img.lermanga.org/B/boku-no-hero-academia/capitulo-"
    
    try:
        st.session_state.capitulo = int(st.text_input("Digite o numero do capitulo"))
        if st.session_state.capitulo != st.session_state.capitulo_antigo :
            st.session_state.page = 1
            st.session_state.capitulo_antigo  = st.session_state.capitulo
            
        if st.session_state.capitulo <=10:
            st.session_state.start_capitulo = "0"
        else:
            st.session_state.start_capitulo = ""

    except:
        st.write("Erro digite um numero")

elif st.session_state.manga == "Jujutsu Kaisen":
    url_base = "https://img.lermanga.org/J/jujutsu-kaisen/capitulo-"
    try:
        st.session_state.capitulo = int(st.text_input("Digite o numero do capitulo"))
        if st.session_state.capitulo <=10:
            st.session_state.start_capitulo = "0"
        else:
            st.session_state.start_capitulo = ""
    except:
        st.write("Erro digite um numero")
    

def render_image():
    st.write(f"Capitulo {st.session_state.capitulo}")
    st.write(f"Pagina {st.session_state.page}")
    try:
        url = f"{url_base}{st.session_state.start_capitulo}{st.session_state.capitulo}/{st.session_state.start_page}{st.session_state.page}.{st.session_state.extension}"
        print(url)
        response = requests.get(url)
        print("response",response.status_code)
        if response.status_code == 200:
            st.image(BytesIO(response.content))
        
        else:
            trocar_type_start_page()
            url = f"{url_base}{st.session_state.start_capitulo}{st.session_state.capitulo}/{st.session_state.start_page}{st.session_state.page}.{st.session_state.extension}"
            print(url)
            response = requests.get(url)
            print("response",response.status_code)
            if response.status_code == 200:
                st.image(BytesIO(response.content))
                

            else:
                trocar_extension()
                url = f"{url_base}{st.session_state.start_capitulo}{st.session_state.capitulo}/{st.session_state.start_page}{st.session_state.page}.{st.session_state.extension}"
                print(url)
                response = requests.get(url)
                print("response",response.status_code)
                if response.status_code == 200:
                    st.image(BytesIO(response.content))
                else:
                    trocar_type_start_page()
                    url = f"{url_base}{st.session_state.start_capitulo}{st.session_state.capitulo}/{st.session_state.start_page}{st.session_state.page}.{st.session_state.extension}"
                    print(url)
                    response = requests.get(url)
                    print("response",response.status_code)
                    if response.status_code == 200:
                        st.image(BytesIO(response.content))

                    else:
                        st.error("Please enter a valid input")
                       
    except:
        st.error("Please enter a valid input")
        # print("rato")
        # try:
        #     trocar_extension()
        #     render_image()
        # except:
        #     trocar_type_start_page()
        #     render_image()
    # print(type(a))

def trocar_type_start_page():
    if st.session_state.start_page == "":
        st.session_state.start_page = "0"
    else:
        st.session_state.start_page = ""


def add_1_page():
    st.session_state.page +=1
def less_1_page():
    if st.session_state.page>1:
        st.session_state.page -=1

# def add_1_cap():
#     st.session_state.capitulo +=1
#     st.session_state.page =1
# def less_1_cap():
#     if st.session_state.capitulo>1:
#         st.session_state.capitulo -=1
#         st.session_state.page=1

def trocar_extension():
    if st.session_state.extension=="png":
        st.session_state.extension= "jpg"
    else:
        st.session_state.extension= "png"

if st.session_state.manga != "None":
    # st.button('Trocar para Jpg ou Png', on_click=trocar_extension)

    # st.button('Voltar Cap', on_click=less_1_cap)
    # st.button('Proximo Cap', on_click=add_1_cap)


    st.button('Voltar imagem', on_click=less_1_page)
    st.button('Proxima imagem', on_click=add_1_page)


    render_image()

