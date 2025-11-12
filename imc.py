import streamlit as st 
import pandas as pd

def imc():
    st.subheader("Indice de Masa Corporal")

    st.latex(r"\text{IMC} = \frac{\text{Peso(kg)}}{\text{Altura(m)}^2}")

    st.markdown("**Tabla del IMC según la OMS**")

    datos_imc = {
        "categoria":[
            "Peso insuficiente",
            "Peso Normal",
            "Sobrepeso",
            "Obesidad grado 1",
            "Obesidad grado 2",
            "Obesidad grado 3 (morbida)",
        ],
        "rango":[
            "Menos de 18.5",
            "18.6 - 24.9",
            "25 - 29.9",
            "30 - 34.9",
            "35 - 39.9",
            "40 - más"
        ]
    }

    tabla_imc = pd.DataFrame(datos_imc)
    st.dataframe(
        datos_imc,
        hide_index=True,
        column_config={
            "categoria":"CATEGORÍA",
            "rango":"RANGO - IMC"
        }
    )

    c1, c2 = st.columns(2)

    peso = c1.number_input("Peso", step=1)
    altura = c2.number_input("Altura")

    def imc_calc(peso, altura):
        if altura <= 0 or peso <= 0:
            return "La altura y el peso deben ser mayores a 0"
        else:
            imc_res = peso / (altura ** 2)
            return f"Tu IMC es: {imc_res:.2f}"
        
    if st.button("Calcular", type="primary"):
        imc = imc_calc(peso,altura)
        st.title(f":green[{imc}]")

