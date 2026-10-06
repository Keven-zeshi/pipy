import pandas as pd
import streamlit as st

# Configuração da página do navegador
st.set_page_config(page_title="Meu App Streamlit", layout="centered")

# Título do Dashboard
st.title("📊 Painel Interativo com Streamlit")
st.write(
    "Este é um aplicativo web completo escrito puramente em Python!"
)

# Criando um estado na sessão para armazenar dados digitados
if "historico" not in st.session_state:
  st.session_state.historico = []

# Criando abas para organizar o conteúdo
aba1, aba2 = st.tabs(["Início", "Visualização de Dados"])

with aba1:
  st.header("Entrada de Informações")

  # Input de texto clássico (com atualização em tempo real ativada)
  nome = st.text_input("Qual é o seu nome?", placeholder="Digite aqui...")

  # Elementos interativos modernos (Slider e Caixas de Seleção)
  idade = st.slider("Selecione sua idade", min_value=0, max_value=100, value=25)
  gosta_python = st.checkbox("Eu gosto de programar em Python 🐍")

  # Botão para salvar as informações no estado da sessão
  if st.button("Salvar Dados"):
    if nome.strip():
      st.session_state.historico.append({
          "Nome": nome,
          "Idade": idade,
          "Python": "Sim" if gosta_python else "Não",
      })
      st.success("Dados salvos com sucesso!")
    else:
      st.warning("Por favor, digite um nome antes de salvar.")

with aba2:
  st.header("Análise e Gráficos")

  if st.session_state.historico:
    # Transforma o histórico guardado em um DataFrame do Pandas
    df = pd.DataFrame(st.session_state.historico)

    # Exibe a tabela interativa (com recursos de ordenação automáticos)
    st.subheader("📋 Usuários Cadastrados")
    st.dataframe(df, use_container_width=True)

    # Gráfico simples baseado na idade dos usuários cadastrados
    st.subheader("📈 Distribuição de Idades")
    st.bar_chart(df, x="Nome", y="Idade")
  else:
    # Feedback visual animado enquanto não há dados carregados
    st.info(
        "Nenhum dado cadastrado ainda. Vá até a aba 'Início' para adicionar informações."
    )
