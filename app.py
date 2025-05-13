# app.py
import pandas as pd 
import streamlit as st
from strem import responder_pergunta  # <-- função que vamos criar

# Carrega o CSV
df = pd.read_csv("R:\\Inovacoes\\Bernardo\\Rep_sitemas\\streamlit\\nomes_aleatorios.csv", delimiter=";")

# Exibe o DataFrame
st.title("Conta df")
st.dataframe(df)

# Input do usuário
query = st.text_area(label="Insira aqui sua pergunta:")

# Se digitar algo, processamos
if query:
    resposta = responder_pergunta(query, df)  # < pergunta e o df
    st.success(resposta)
