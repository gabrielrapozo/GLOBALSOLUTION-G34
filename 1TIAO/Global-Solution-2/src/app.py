import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# ==========================================
# Configuração da Página
# ==========================================
st.set_page_config(page_title="OmniSat-AI | Análise Robusta", layout="wide")

@st.cache_data
def carregar_dados():
    try:
        return pd.read_csv("omnisat_avancado.csv")
    except FileNotFoundError:
        return pd.DataFrame()

df = carregar_dados()

if df.empty:
    st.error("⚠️ Base de dados não encontrada! Rode 'python backend.py' no terminal primeiro.")
else:
    st.sidebar.title("🛰️ OmniSat-AI Avançado")
    pagina = st.sidebar.radio(
        "Navegação:",
        ["Dashboard Geral", "Análises Estatísticas", "Visão Computacional (IA)", "Orquestração AWS"]
    )

    # ==========================================
    # Tela 1: Dashboard Geral
    # ==========================================
    if pagina == "Dashboard Geral":
        st.header("Monitoramento Integrado Socioambiental")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Regiões Monitoradas", len(df['regiao'].unique()))
        col2.metric("Pico de Chuva (24h)", f"{df['precipitacao_mm'].max()} mm")
        col3.metric("Risco Médio Atual", f"{round(df['score_risco'].mean(), 1)} / 100")
        col4.metric("Alertas Críticos", len(df[df['status_ia'] == 'CRÍTICO - Evacuação']))
        
        st.subheader("Evolução Temporal do Score de Risco")
        fig_linha = px.line(df, x="data_hora", y="score_risco", color="regiao", 
                           title="Comparativo de Risco entre Áreas com Diferentes IDHs e Relevos")
        st.plotly_chart(fig_linha, use_container_width=True)

    # ==========================================
    # Tela 2: Análises Estatísticas
    # ==========================================
    elif pagina == "Análises Estatísticas":
        st.header("📊 Correlação: Fatores Geográficos vs Desastres Naturais")
        st.write("Análise estatística relacionando indicadores socioeconômicos (IDH, Pobreza) e físicos (Inclinação, Chuva) com o Score de Risco.")
        
        colunas_corr = ['score_risco', 'precipitacao_mm', 'umidade_solo_pct', 
                        'inclinacao_graus', 'construcao_irregular_pct', 'idh', 'indice_pobreza_pct']
        matriz_corr = df[colunas_corr].corr()
        
        col_esq, col_dir = st.columns([1, 1])
        
        with col_esq:
            st.subheader("Matriz de Correlação (Heatmap)")
            fig_corr = px.imshow(matriz_corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                                 title="Impacto das variáveis no Risco (1.0 = Correlação Máxima)")
            # ERRO CORRIGIDO AQUI (Parêntesis fechado corretamente):
            st.plotly_chart(fig_corr, use_container_width=True)
            
        with col_dir:
            st.subheader("Construção Irregular vs Risco Máximo")
            fig_scatter = px.scatter(df, x="construcao_irregular_pct", y="score_risco", color="regiao",
                                     size="indice_pobreza_pct", hover_data=["idh"],
                                     title="Relação entre Moradia Irregular e Risco de Desastre")
            st.plotly_chart(fig_scatter, use_container_width=True)

    # ==========================================
    # Tela 3: Visão Computacional (Mapa Satélite Interativo)
    # ==========================================
    elif pagina == "Visão Computacional (IA)":
        st.header("👁️ Análise Orbital Interativa (Segmentação de IA)")
        st.write("A plataforma processa as imagens do satélite em tempo real. As caixas coloridas simulam o algoritmo de Inteligência Artificial segmentando anomalias construtivas e estresse hídrico.")
        
        # Coordenadas de exemplo (Rio de Janeiro)
        lat_base, lon_base = -22.9068, -43.1729
        
        # Criando o mapa focado nas coordenadas
        mapa_orbital = folium.Map(location=[lat_base, lon_base], zoom_start=13, tiles=None)
        
        # Adicionando a camada REAL de satélite da Esri (Não é bloqueada pelo Python)
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Esri Satellite',
            overlay=False,
            control=True
        ).add_to(mapa_orbital)
        
        # Simulação IA 1: Bounding Box Vermelha - Risco Urbano (ODS 11)
        folium.Rectangle(
            bounds=[[lat_base - 0.01, lon_base - 0.015], [lat_base + 0.01, lon_base - 0.005]],
            color='#FF0000',
            fill=True,
            fill_color='#FF0000',
            fill_opacity=0.3,
            popup='CRÍTICO: Alta densidade irregular + Inclinação severa (ODS 11)',
            tooltip='Área de Risco: Clique para detalhes'
        ).add_to(mapa_orbital)

        # Simulação IA 2: Bounding Box Amarela - Risco Agrícola (ODS 2)
        folium.Rectangle(
            bounds=[[lat_base - 0.02, lon_base + 0.01], [lat_base - 0.005, lon_base + 0.025]],
            color='#FFD700',
            fill=True,
            fill_color='#FFD700',
            fill_opacity=0.3,
            popup='ALERTA: Queda no índice NDVI detectada (Estresse Hídrico - ODS 2)',
            tooltip='Área Agrícola: Clique para detalhes'
        ).add_to(mapa_orbital)

        # Renderizando o mapa no Streamlit
        st_folium(mapa_orbital, width=1000, height=500)
        st.caption("Nota técnica: Imagens renderizadas via Esri World Imagery API. As geometrias sobrepostas simulam a saída de uma rede neural (YOLO/U-Net).")

    # ==========================================
    # Tela 4: Orquestração AWS
    # ==========================================
    elif pagina == "Orquestração AWS":
        st.header("☁️ Logs de Decisão AWS")
        st.write("Histórico do pipeline serverless processando os alertas gerados.")
        st.dataframe(df[['data_hora', 'regiao', 'score_risco', 'alerta_sns']].tail(15), use_container_width=True)