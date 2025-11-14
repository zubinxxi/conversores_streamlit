import os
import streamlit as st 
import requests as rq
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("API_KEY")


#https://apilayer.net/api/live?access_key=b99fa0112782991a9bd2bd95ad2affee&currencies=EUR&source=USD&format=1

def cambio():
    st.subheader("Conversor de Monedas")
    #st.write(API_KEY)

    currencies = [
        ('USD', 'Dólar Estadounidense'),
        ('EUR', 'Euro'),
        ('JPY', 'Yen Japonés'),
        ('GBP', 'Libra Esterlina'),
        ('AUD', 'Dólar Australiano'),
        ('CAD', 'Dólar Canadiense'),
        ('CHF', 'Franco Suizo'),
        ('CNY', 'Yuan Chino'),
        ('MXN', 'Peso Mexicano'),
        ('BRL', 'Real Brasileño'),
    ]

    cc1, cc2, cc3 = st.columns(3)
    moneda = cc1.number_input("moneda", step=1, value=1)
    with cc2:
        moneda_origen = st.selectbox("Moneda origen", options=[item[1] for item in currencies])
        codigo_origen = next(item[0] for item in currencies if item[1] == moneda_origen)
        #st.write(f"({codigo_origen})")

    with cc3:
        moneda_destino = st.selectbox("Moneda destino", options=sorted([item[1] for item in currencies]))
        codigo_destino = next(item[0] for item in currencies if item[1] == moneda_destino)
        #st.write(f"({codigo_destino})")

    url = f"https://apilayer.net/api/live?access_key={api_key}&currencies={codigo_destino}&source={codigo_origen}&format=1"
    
    if st.button("Convertir", type="primary", key="btn_cambio"):
        response = rq.get(url)
        data = response.json()
        tipo_cambio = data['quotes'][f'{codigo_origen}{codigo_destino}']
        res_moneda = moneda * tipo_cambio

        st.subheader(f"{moneda} {moneda_origen} equivale a: :red[{res_moneda:,.2f}] {moneda_destino}")