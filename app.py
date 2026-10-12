from datetime import datetime
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Busca Inteligente", page_icon="", layout="wide"
)


# Estilo CSS para o Botão Azul
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #004d99;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Coloque esta parte onde você quiser que a imagem apareça
try:

# Coloque o nome do arquivo da imagem que está na sua pasta (ex: 'meme.png' ou 'avatar.jpg')
  st.image(
      "imagem_divertida.jpg",
      width=500,
  )
except Exception:
  pass
st.title("Busca Inteligente")
st.markdown(
    "Escolha o produto que você deseja e escolha o valor que caiba no seu bolso."
)

# Organização em 3 colunas (Produto, Preço e Seleção de Site)
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
  termo_busca = st.text_input(
      "O que você está procurando?",
      placeholder="Ex: PlayStation 5 Slim, Notebook Gamer...",
  )

with col2:
  preco_maximo = st.number_input(
      "Escolha um valor: (R$)", min_value=0.0, value=5000.0, step=100.0
  )

with col3:
  site_escolhido = st.selectbox(
      "Escolha a Loja:", ["Mercado Livre", "Amazon", "Magalu"]
  )

# Botão de Ação Principal
if st.button("Buscar e Filtrar Ofertas", use_container_width=True):
  if termo_busca.strip():
    with st.spinner(f"Gerando link otimizado para {site_escolhido}..."):
      termo_formatado = termo_busca.replace(" ", "-")

      # Define a URL de acordo com a loja escolhida
      if site_escolhido == "Mercado Livre":
        url_busca = f"https://lista.mercadolivre.com.br/{termo_formatado}"
      elif site_escolhido == "Amazon":
        url_busca = f"https://www.amazon.com.br/s?k={termo_busca.replace(' ', '+')}"
      elif site_escolhido == "Magalu":
        url_busca = f"https://www.magazineluiza.com.br/busca/{termo_formatado}/"

      data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    st.success("Busca processada com sucesso!")

    st.markdown(f"###  Oferta Principal Encontrada na {site_escolhido}")
    st.info(
        f"**Loja:** {site_escolhido} \n\n**Produto:** {termo_busca.title()}"
        f" \n\n**Orçamento Limite:** R$ {preco_maximo:,.2f}"
    )
    st.link_button(f"Acessar Resultados na {site_escolhido} ", url_busca)

  else:
    st.warning("Por favor, digite o nome de um produto.")


# Rodapé
st.markdown(
    "<p style='text-align: center; color: gray;'>Desenvolvido por Vinicius |"
    " Versão teste! </p>",
    unsafe_allow_html=True,
)
