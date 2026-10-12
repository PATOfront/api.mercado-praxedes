from datetime import datetime
import streamlit as st

# Configuração da página (deve ser a primeira instrução do Streamlit)
st.set_page_config(
    page_title="Busca Inteligente",
    page_icon="🔍",
    layout="centered"
)

# Estilização CSS avançada + HTML estruturado
st.markdown("""
<style>
    /* Importa a fonte moderna Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Aplica a fonte geral */
    html, body, [class*="st"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Container Principal do Cabeçalho (Hero Section) */
    .hero-container {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
        background: linear-gradient(135deg, rgba(51, 153, 255, 0.05) 0%, rgba(0, 77, 153, 0.1) 100%);
        border-radius: 16px;
        border: 1px solid rgba(51, 153, 255, 0.2);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 42px !important;
        font-weight: 700 !important;
        color: #3399ff !important;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 16px !important;
        color: #d1d5db !important;
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Padronização dos Inputs e Selectbox */
    .stTextInput input, 
    .stNumberInput input,
    div[data-baseweb="select"] > div {
        background-color: #2b2b2b !important;
        border: 1px solid #4e4c4c !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        height: 48px !important;
        box-sizing: border-box !important;
    }

    div[data-baseweb="select"] {
        background-color: transparent !important;
    }

    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    /* Foco nos inputs */
    .stTextInput input:focus, 
    .stNumberInput input:focus, 
    div[data-baseweb="select"] > div:focus-within {
        border-color: #3399ff !important;
        box-shadow: 0 0 0 2px rgba(51, 153, 255, 0.2) !important;
    }

    /* Botão Principal Estilizado */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0066cc 0%, #004d99 100%) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        height: 48px !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
        transition: all 0.3s ease;
    }

    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #0073e6 0%, #003d80 100%) !important;
        box-shadow: 0 6px 16px rgba(0, 102, 204, 0.5);
        transform: translateY(-1px);
    }
</style>

<!-- Cabeçalho em HTML puro perfeitamente centralizado e estruturado -->
<div class="hero-container">
    <div class="hero-title">🔍 Busca Inteligente</div>
    <div class="hero-subtitle">Escolha o produto que você deseja e escolha o valor que caiba no seu bolso, comparando os melhores do mercado digital num só lugar.</div>
</div>
""", unsafe_allow_html=True)

# Organização em 3 colunas (Produto, Preço e Seleção de Site)
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    termo_busca = st.text_input(
        "O que você está procurando?",
        placeholder="Ex: Camisa, cafeteira, fone, smartphone...",
    )

with col2:
    preco_maximo = st.number_input(
        "Escolha um valor: (R$)", min_value=0.0, value=5000.0, step=100.0
    )

with col3:
    site_escolhido = st.selectbox(
        "Escolha a Loja:", ["Mercado Livre", "Amazon", "Magalu", "Shopee"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# Botão de Ação Principal
if st.button("Buscar e Filtrar Produtos", use_container_width=True):
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
            elif site_escolhido == "Shopee":
                url_busca = f"https://shopee.com.br/search?keyword={termo_formatado}"

            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        st.success("Busca processada com sucesso!")

        st.markdown(f"### Produto encontrado na {site_escolhido}")
        st.info(
            f"**Loja:** {site_escolhido} \n\n**Produto:** {termo_busca.title()}"
            f" \n\n**Preço:** R$ {preco_maximo:,.2f}"
        )
        st.link_button(f"Acessar Resultados na {site_escolhido}", url_busca)

    else:
        st.warning("Por favor, digite o nome do produto que você procura.")

# Rodapé
st.markdown("<br><hr style='border:0; border-top:1px solid #333;'><p style='text-align: center; color: #777; font-size: 13px;'>Desenvolvido por Vinicius | Versão teste!</p>", unsafe_allow_html=True)
