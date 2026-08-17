import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# 1. Configuration de la page (Doit être la première commande)
st.set_page_config(page_title="Dashboard Carrière - Amani Tlili", layout="wide", initial_sidebar_state="expanded")

# 2. Optimisation : Mise en cache des données
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"Tâche": "Baccalauréat en informatique", "Début": "2010-09-01", "Fin": "2013-06-01", "Catégorie": "Formation"},
        {"Tâche": "Maîtrise : Génie logiciel", "Début": "2013-09-01", "Fin": "2015-06-01", "Catégorie": "Formation"},
        {"Tâche": "Développeuse web & designer", "Début": "2015-08-01", "Fin": "2019-04-01", "Catégorie": "Expérience"},
        {"Tâche": "Enseignante", "Début": "2016-09-01", "Fin": "2019-07-01", "Catégorie": "Expérience"},
        {"Tâche": "Maîtrise : Multimédia & Web", "Début": "2017-09-01", "Fin": "2020-06-01", "Catégorie": "Formation"},
        {"Tâche": "Agente de voyages", "Début": "2024-08-01", "Fin": "2025-02-01", "Catégorie": "Expérience"},
        {"Tâche": "Certificat : Exploitation des données (HEC)", "Début": "2026-01-01", "Fin": "2026-12-31", "Catégorie": "Formation"}
    ])

df_timeline = load_data()

# 3. Barre latérale (Sidebar) - Filtres interactifs
st.sidebar.header("⚙️ Contrôles interactifs")
st.sidebar.markdown("Filtrez les données du parcours :")
show_exp = st.sidebar.checkbox("Afficher les Expériences", value=True)
show_form = st.sidebar.checkbox("Afficher les Formations", value=True)

# Application des filtres sur le DataFrame
categories_to_show = []
if show_exp: categories_to_show.append("Expérience")
if show_form: categories_to_show.append("Formation")
df_filtered = df_timeline[df_timeline["Catégorie"].isin(categories_to_show)]

st.sidebar.markdown("---")
st.sidebar.subheader("📥 Document officiel")

# Bouton de téléchargement du CV (Vérification de l'existence du fichier)
cv_file_path = "Amani_Tlili_CV_Spontanee_Final.pdf"
if os.path.exists(cv_file_path):
    with open(cv_file_path, "rb") as pdf_file:
        st.sidebar.download_button(
            label="📄 Télécharger le CV (PDF)",
            data=pdf_file,
            file_name="Amani_Tlili_CV_Analyste.pdf",
            mime="application/pdf",
            use_container_width=True
        )
else:
    st.sidebar.error("Fichier PDF non trouvé dans le répertoire.")

# 4. En-tête principal
st.title("📊 Tableau de Bord Professionnel - Amani Tlili")
st.markdown("### Analyste de Données / Analyste d'Affaires")
st.markdown("📍 Montréal, QC | 📞 (438) 855-1310 | ✉️ ameni1tlili@gmail.com | 🔗 [LinkedIn](https://linkedin.com/in/amanitlili/)")
st.markdown("---")

# 5. Synthèse Professionnelle
st.subheader("📝 Synthèse Professionnelle")
st.info("Étudiante au certificat en exploitation des données à HEC Montréal et titulaire de deux maîtrises en informatique, je possède une solide base en développement logiciel, en méthodologies Agiles et en analyse de données (SQL, Python, ETL). Possédant une expérience concrète dans la collecte de besoins d'affaires, la modélisation de bases de données et la documentation technique, je souhaite mettre mes compétences au service d'initiatives technologiques visant à optimiser les processus et à valoriser les données au sein d'une organisation innovante.")

# 6. Métriques clés (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Diplômes Universitaires", "3", "Informatique & Data")
col2.metric("Certifications Obtenues", "5", "Microsoft & Univ. of Michigan")
col3.metric("Années d'Expérience", "7+", "TI & Enseignement")
col4.metric("Langues Maîtrisées", "3", "FR, AR, EN")

st.markdown("---")

# 7. Visualisations (Graphiques)
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🗓️ Chronologie du Parcours")
    if not df_filtered.empty:
        fig_timeline = px.timeline(
            df_filtered, 
            x_start="Début", 
            x_end="Fin", 
            y="Tâche", 
            color="Catégorie",
            color_discrete_map={"Formation": "#00A3E0", "Expérience": "#0033A0"},
            template="plotly_white"
        )
        fig_timeline.update_yaxes(autorange="reversed")
        fig_timeline.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_timeline, use_container_width=True)
    else:
        st.warning("Veuillez sélectionner au moins une catégorie dans la barre latérale pour afficher la chronologie.")

with col_right:
    st.subheader("🎯 Cartographie des Compétences")
    categories = ['Bases de données (SQL, ETL)', 'Prog. & Data Science (Python)', 
                  'Visualisation (Power BI)', 'Analyse d\'Affaires (Agile, UML)', 
                  'Orientation Client']
    niveaux = [90, 85, 95, 90, 80]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=niveaux + [niveaux[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(0, 163, 224, 0.4)',
        line=dict(color='#0033A0'),
        name='Niveau de maîtrise',
        hoverinfo="r+theta"
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        height=400,
        margin=dict(l=40, r=40, t=30, b=30)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("---")

# 8. Certifications
st.subheader("🏆 Certifications Officielles (2025)")
cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.markdown("**Microsoft**")
    st.success("✅ Harnessing the Power of Data with Power BI\n\n✅ Preparing Data for Analysis with Microsoft Excel")

with cert_col2:
    st.markdown("**University of Michigan**")
    st.success("✅ Building Database Applications in PHP\n\n✅ JavaScript, jQuery, and JSON\n\n✅ Des applications web pour tous")
