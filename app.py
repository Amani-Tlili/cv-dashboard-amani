import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from PIL import Image

# 1. Configuration (Doit être la première ligne)
st.set_page_config(page_title="Amani Tlili - Dashboard CV", layout="wide", initial_sidebar_state="collapsed")

# 2. Injection de CSS pour le design "Dark SlideModel"
st.markdown("""
<style>
    /* Fond général sombre (Gris anthracite/Bleu nuit) */
    .stApp {
        background-color: #1A1D24;
    }
    
    /* Typographie */
    h1, h2, h3, h4, p, span {
        color: #E2E8F0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Couleur d'accentuation (Cyan technologique) */
    .highlight {
        color: #00D2FF !important;
    }

    /* Style de la colonne Profil (gauche) pour créer un effet "Carte" */
    [data-testid="column"]:nth-child(1) {
        background-color: #222631;
        padding: 30px 20px;
        border-radius: 15px;
        border-top: 4px solid #00D2FF;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
    }

    /* Style des conteneurs de métriques (KPIs) */
    div[data-testid="metric-container"] {
        background-color: #222631;
        border-radius: 10px;
        padding: 15px;
        border-left: 4px solid #00D2FF;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    [data-testid="stMetricValue"] {
        color: #00D2FF !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Données (Extraites de votre CV)
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"Tâche": "Baccalauréat Informatique", "Début": "2010-09-01", "Fin": "2013-06-01", "Catégorie": "Formation"},
        {"Tâche": "Maîtrise: Génie logiciel", "Début": "2013-09-01", "Fin": "2015-06-01", "Catégorie": "Formation"},
        {"Tâche": "Développeuse web", "Début": "2015-08-01", "Fin": "2019-04-01", "Catégorie": "Expérience"},
        {"Tâche": "Enseignante", "Début": "2016-09-01", "Fin": "2019-07-01", "Catégorie": "Expérience"},
        {"Tâche": "Maîtrise: Multimédia", "Début": "2017-09-01", "Fin": "2020-06-01", "Catégorie": "Formation"},
        {"Tâche": "Agente de voyages", "Début": "2024-08-01", "Fin": "2025-02-01", "Catégorie": "Expérience"},
        {"Tâche": "Certificat: Exploitation données", "Début": "2026-01-01", "Fin": "2026-12-31", "Catégorie": "Formation"}
    ])

df_timeline = load_data()

# 4. Structure de la page : 1/3 pour le profil, 2/3 pour les données
col_profil, col_donnees = st.columns([1, 2.5], gap="large")

# ==========================================
# COLONNE DE GAUCHE : PROFIL (Style Sidebar)
# ==========================================
with col_profil:
    if os.path.exists("photo_profil.png"):
        img = Image.open("photo_profil.png")
        st.image(img, use_container_width=True)
    else:
        st.markdown("<div style='height: 150px; background-color:#1A1D24; border-radius:10px; text-align:center; line-height:150px;'>[Zone Photo]</div>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Amani <span class='highlight'>Tlili</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1rem; color: #A0AAB2 !important;'>Analyste de Données / Affaires</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📞 Contact")
    st.markdown("📱 (438) 855-1310<br>📧 ameni1tlili@gmail.com<br>📍 Montréal, QC<br>🔗 [LinkedIn](https://linkedin.com/in/amanitlili/)", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 💡 À propos")
    st.markdown("""
    <p style='font-size: 0.9rem; text-align: justify;'>Étudiante au certificat en exploitation des données à HEC Montréal et titulaire de deux maîtrises en informatique[cite: 1]. Profil hybride alliant développement logiciel, méthodologies Agiles et analyse de données (SQL, Python, ETL)[cite: 1].</p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    cv_file_path = "Amani_Tlili_CV_Spontanee_Final.pdf"
    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            st.download_button(label="📥 Télécharger CV (PDF)", data=pdf_file, file_name="Amani_Tlili_CV.pdf", mime="application/pdf", use_container_width=True)

# ==========================================
# COLONNE DE DROITE : ANALYTIQUE
# ==========================================
with col_donnees:
    # Ligne 1 : Les KPIs
    st.markdown("### Aperçu des performances")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Années d'expérience", "7+", "Développement & Analyse")
    kpi2.metric("Diplômes Universitaires", "3", "Info & Data")
    kpi3.metric("Certifications (2025)", "5", "Microsoft & Michigan")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Ligne 2 : Les compétences (Graphique à barres horizontales style SlideModel)
    st.markdown("### 🛠️ Expertise Technique")
    competences = ['UML & Agilité', 'Python & Pandas', 'ETL & Nettoyage', 'Power BI & Visualisation', 'Bases de données (SQL)']
    niveaux = [85, 80, 85, 95, 95]
    
    fig_bar = px.bar(
        x=niveaux, y=competences, orientation='h', 
        color_discrete_sequence=['#00D2FF']
    )
    fig_bar.update_layout(
        xaxis_title="Niveau de maîtrise (%)", yaxis_title="",
        xaxis=dict(range=[0, 100], showgrid=True, gridcolor='#2D3342'),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='#E2E8F0'), height=250, margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Ligne 3 : La chronologie
    st.markdown("### 🗓️ Ligne du temps du parcours")
    fig_timeline = px.timeline(
        df_timeline, x_start="Début", x_end="Fin", y="Tâche", color="Catégorie",
        color_discrete_map={"Formation": "#00D2FF", "Expérience": "#6C63FF"} 
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='#E2E8F0'),
        xaxis=dict(showgrid=True, gridcolor='#2D3342'),
        height=300, margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
