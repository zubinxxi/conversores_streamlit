import streamlit as st 
from imc import imc
from conversor import conversor
from cambio import cambio

st.set_page_config(
    "Conversores",
    page_icon="assets/favicon.ico",
)

st.title(":green[Calculos y Conversores]")

tab1, tab2, tab3 = st.tabs(
    [
        "IMC",
        "Conversor de Unidades",
        "Conversor de Monedas"
    ]
)

with tab1:
    imc()

with tab2:
    conversor()

with tab3:
    cambio()
