import streamlit as st
from transformers import pipeline

st.title("Análise de Sentimento")

texto = st.text_input("Digite um texto/sentimento em inglês:")

sentiment_classifier = pipeline("sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")

if (texto):
    resultado = sentiment_classifier(texto)
    if(resultado[0]["label"] == "POSITIVE"):
        st.write(f"Este é um sentimento positivo :)  \n {resultado[0]["score"]:.1%} de confiança neste sentimento")
    else:
        st.write(f"Este é um sentimento negativo :(  \n {resultado[0]["score"]:.1%} de confiança neste sentimento")
    