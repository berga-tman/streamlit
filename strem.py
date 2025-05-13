import pandas as pd 
import streamlit as st


def responder_pergunta(pergunta, df):
    pergunta = pergunta.lower()

    if "quantas linhas" in pergunta:
        return f"O DataFrame tem {len(df)} linhas."

    elif "colunas" in pergunta:
        return f"As colunas são: {', '.join(df.columns)}"

    elif "nulo" in pergunta or "faltando" in pergunta:
        nulos = df.isnull().sum()
        return f"Valores nulos por coluna:\n{nulos.to_string()}"

    else:
        return "Desculpe, não entendi a pergunta. Tente algo como: 'quantas linhas tem?' ou 'tem dados faltando?'."

# app.py