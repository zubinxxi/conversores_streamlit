import streamlit as st 
from streamlit_extras.no_default_selectbox import selectbox as no_df_selectbox

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
    with col1:
        valor = col1.number_input("introduce el valor a convertir", min_value=0.0, value=1.0)
    with col2:    
        origen = no_df_selectbox("Unidad de origen", options=unidades, placeholder="Select", no_selection_label="Seleccionar")
    with col3:
        destino = no_df_selectbox("Unidad de destino", options=unidades, placeholder="Select", no_selection_label="Seleccionar")

    if st.button("Convertir", type="primary"):
        resultado = conversor_unidades(valor, origen, destino)
        st.subheader(f"{valor:,.2f} {origen} son equivalentes a: {resultado:,.2f} {destino}")