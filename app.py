import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from PIL import Image

# 1. Configuration (Doit être la première ligne)
st.set_page_config(page_title="Dashboard Carrière - Amani Tlili", layout="wide", initial_sidebar_state="collapsed")

# 2. Injection de CSS personnalisé pour un design "Relaxant et Aéré"
st.markdown("""
<style>
    /* Couleur de fond globale douce */
    .stApp {
        background-color: #F4F7F6;
    }
    
    /* Typographie globale */
    h1, h2, h3, p {
        color: #2C3E50;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Style des "Cartes" pour les métriques */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        border: 1px solid #E8EEF2;
    }
    
    /* Espacement et style des conteneurs de graphiques */
    .stPlotlyChart {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# 3. Données en cache
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

# 4. En-tête : Profil (Photo + Intro + KPIs)
col_photo, col_intro, col_kpi1, col_kpi2 = st.columns([1, 2.5, 1, 1])

with col_photo:
    # Affiche la photo si elle existe, sinon un espace vide
    if os.path.exists("photo_profil.jpg"):
        img = Image.open("photo_profil.jpg")
        st.image(img, use_container_width=True)
    else:
        st.info("Insérez 'photo_profil.png' dans le dossier.")

with col_intro:
    st.markdown("<h1>AMANI TLILI</h1>", unsafe_allow_html=True)
    st.markdown("### Analyste de Données / Analyste d'Affaires")
    st.markdown("📍 Montréal, QC | 📞 (438) 855-1310 | ✉️ ameni1tlili@gmail.com")
    st.markdown("*Hybride : Développement Logiciel & Data Science[cite: 1].*")

with col_kpi1:
    st.metric("Expérience Cumulée", "7+ Ans", "Développement & Analyse")
    
with col_kpi2:
    st.metric("Certifications", "5", "Microsoft & Univ. Michigan")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Section Centrale : Timeline et Compétences
col_gantt, col_radar = st.columns([1.5, 1])

with col_gantt:
    st.markdown("### 🗓️ Évolution du Parcours")
    fig_timeline = px.timeline(
        df_timeline, x_start="Début", x_end="Fin", y="Tâche", color="Catégorie",
        # Couleurs douces : Bleu pastel et Vert d'eau
        color_discrete_map={"Formation": "#5C9EAD", "Expérience": "#75B9BE"}, 
        template="plotly_white"
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(
        height=350, margin=dict(l=0, r=0, t=10, b=0),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

with col_radar:
    st.markdown("### 🎯 Architecture des Compétences")
    categories = ['Bases de données (SQL)', 'Python & ETL', 'Visualisation (Power BI)', 'Analyse d\'Affaires (UML)', 'Agilité']
    niveaux = [95, 85, 95, 90, 90]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=niveaux + [niveaux[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(92, 158, 173, 0.5)', # Bleu pastel transparent
        line=dict(color='#326273'), # Bordure plus foncée
        hoverinfo="r+theta"
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=False, range=[0, 100])),
        showlegend=False, height=350, margin=dict(l=40, r=40, t=10, b=30),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Section Inférieure : Téléchargement et Détails
col_desc, col_download = st.columns([2, 1])

with col_desc:
    st.markdown("### 💡 Synthèse Professionnelle")
    st.markdown("""
    Étudiante au certificat en exploitation des données à HEC Montréal et titulaire de deux maîtrises en informatique, je possède une solide base en développement logiciel, en méthodologies Agiles et en analyse de données (SQL, Python, ETL)[cite: 1].  
    Je souhaite mettre mes compétences au service d'initiatives technologiques visant à optimiser les processus et à valoriser les données au sein d'une organisation innovante[cite: 1].
    """)

with col_download:
    st.markdown("### 📥 Document Complet")
    st.markdown("Téléchargez la version détaillée de mon profil incluant toutes mes expériences techniques.")
    cv_file_path = "Amani_Tlili_CV_Spontanee_Final.pdf"
    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Télécharger le CV (PDF)",
                data=pdf_file,
                file_name="Amani_Tlili_CV_Analyste.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("Fichier PDF non trouvé.")
