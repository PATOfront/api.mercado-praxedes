from datetime import datetime
import os
import pandas as pd
import streamlit as st

# Configuração da página (deve ser a primeira instrução do Streamlit)
st.set_page_config(
    page_title="Busca Inteligente",
    page_icon="🔍",
    layout="centered"
)

# ========================================================
# FUNÇÃO PARA SALVAR O HISTÓRICO DE BUSCAS DE FORMA SEGURA
# ========================================================
def salvar_historico(produto, preco_min, preco_max, loja):
    try:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        novo_registro = {
            "Data/Hora": [data_hora],
            "Produto": [produto],
            "Preço Mín (R$)": [preco_min],
            "Preço Máx (R$)": [preco_max],
            "Loja": [loja]
        }
        
        df_novo = pd.DataFrame(novo_registro)
        arquivo = "historico_buscas.csv"
        
        if os.path.exists(arquivo):
            df_novo.to_csv(arquivo, mode='a', header=False, index=False, encoding='utf-8-sig')
        else:
            df_novo.to_csv(arquivo, mode='w', header=True, index=False, encoding='utf-8-sig')
            
    except Exception as e:
        print(f"Erro ao salvar histórico: {e}")

# Estilização limpa e segura
st.markdown("""
<style>
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
</style>

<div class="hero-container">
    <div class="hero-title">🔍 Busca Inteligente</div>
    <div class="hero-subtitle">Escolha o produto que você deseja, defina a sua faixa de preço ideal e compare os melhores produtos do mercado digital num só lugar.</div>
</div>
""", unsafe_allow_html=True)

# Organização em colunas para os filtros
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    termo_busca = st.text_input(
        "O que você está procurando?",
        placeholder="Ex: Camisa, cafeteira, fone...",
    )

with col2:
    preco_minimo = st.number_input(
        "Preço Mín: (R$)", min_value=0.0, value=0.0, step=50.0
    )

with col3:
    preco_maximo = st.number_input(
        "Preço Máx: (R$)", min_value=0.0, value=5000.0, step=100.0
    )

with col4:
    site_escolhido = st.selectbox(
        "Escolha a Loja:", ["Mercado Livre", "Amazon", "Magalu", "Shopee"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# Botão de Ação Principal
if st.button("Buscar e Filtrar Produtos", use_container_width=True):
    if termo_busca.strip():
        # Salva o histórico corretamente com as variáveis de preço
        salvar_historico(termo_busca, preco_minimo, preco_maximo, site_escolhido)

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

        st.success("Busca processada com sucesso!")

        st.markdown(f"### Produto encontrado na {site_escolhido}")
        st.info(
            f"**Loja:** {site_escolhido} \n\n**Produto:** {termo_busca.title()}"
            f" \n\n**Faixa de Preço:** R$ {preco_minimo:,.2f} até R$ {preco_maximo:,.2f}"
        )
        st.link_button(f"Acessar Resultados na {site_escolhido}", url_busca)

    else:
        st.warning("Por favor, digite o nome do produto que você procura.")

# ========================================================
# PAINEL DE ADMIN DISCRETO NO RODAPÉ
# ========================================================
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("⚙️ Administração"):
    senha_digitada = st.text_input("Digite a senha de administrador:", type="password", key="senha_admin")
    SENHA_MESTRE = "admin123"
    
    if senha_digitada == SENHA_MESTRE:
        st.success("Acesso autorizado!")
        arquivo_historico = "historico_buscas.csv"
        
        if os.path.exists(arquivo_historico):
            df_historico = pd.read_csv(arquivo_historico)
            st.metric("Total de Buscas Realizadas", len(df_historico))
            st.dataframe(df_historico, use_container_width=True)
            
            st.download_button(
                label="📥 Baixar Histórico em CSV",
                data=df_historico.to_csv(index=False).encode('utf-8-sig'),
                file_name="historico_buscas.csv",
                mime="text/csv"
            )
        else:
            st.info("Ainda não existem registos de busca.")
            
    elif senha_digitada:
        st.error("Senha incorreta.")

# Rodapé
st.markdown("<br><hr style='border:0; border-top:1px solid #333;'><p style='text-align: center; color: #777; font-size: 13px;'>Desenvolvido por Vinicius | Versão teste!</p>", unsafe_allow_html=True)

# Rodapé
st.markdown("<br><hr style='border:0; border-top:1px solid #333;'><p style='text-align: center; color: #777; font-size: 13px;'>Desenvolvido por Vinicius | Versão teste!</p>", unsafe_allow_html=True)
