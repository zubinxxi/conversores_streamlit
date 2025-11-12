import streamlit as st 

def conversor():
    st.subheader("Conversor de Unidades")

    def conversor_unidades(valor, origen, destino):
        conversion_unidades = {
            "Milímetros":0.1,
            "Centímetros":1,
            "Metros":100,
            "Kilómetros":100000
        }

        valor_centimetros = valor * conversion_unidades[origen]
        result = valor_centimetros / conversion_unidades[destino]
        return result
    
    unidades = [
        "Milímetros",
        "Centímetros",
        "Metros",
        "Kilómetros"
    ]

    col1, col2, col3 = st.columns(3)
    valor = col1.number_input("introduce el valor a convertir", min_value=0.0, value=1.0)
    origen = col2.selectbox("Unidad de origen", options=unidades)
    destino = col3.selectbox("Unidad de destino", options=unidades)

    if st.button("Convertir", type="primary"):
        resultado = conversor_unidades(valor, origen, destino)
        st.subheader(f"{valor:,.2f} {origen} son equivalentes a: {resultado:,.2f} {destino}")