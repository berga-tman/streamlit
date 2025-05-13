Este é um pequeno projeto em Python com Streamlit que permite ao usuário fazer perguntas sobre um conjunto de dados (CSV) e obter respostas automáticas com base no conteúdo do arquivo.

---
- Carrega um arquivo CSV (`nomes_aleatorios.csv`) contendo dados.
- Mostra o DataFrame na interface.
- Permite ao usuário digitar uma pergunta sobre os dados.
- Retorna uma resposta automática com base em regras definidas no script `strem.py`.

projeto/
├── app.py # Script principal que roda o Streamlit
├── strem.py # Módulo com a lógica de respostas
├── nomes_aleatorios.csv # Arquivo de dados usado no app

1. Instale o Streamlit e o pandas (caso ainda não tenha):

pip install streamlit pandas


2 No terminal, navegue até a pasta do projeto e execute:
streamlit run app.py
