import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuration de la page
st.set_page_config(page_title="Dashboard Carrière - Amani Tlili", layout="wide", initial_sidebar_state="collapsed")

# 2. En-tête du Dashboard
st.title("📊 Tableau de Bord Professionnel - Amani Tlili")
st.markdown("### Analyste de Données / Analyste d'Affaires")
st.markdown("📍 Montréal, QC | 📞 (438) 855-1310 | ✉️ ameni1tlili@gmail.com | 🔗 linkedin.com/in/amanitlili/")
st.markdown("---")

# 3. Métriques clés (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Diplômes Universitaires", "3", "Informatique & Data")
col2.metric("Certifications Obtenues", "5", "Microsoft & Univ. of Michigan")
col3.metric("Années d'Expérience (TI & Enseignement)", "7+", "Intermédiaire")
col4.metric("Langues Maîtrisées", "3", "FR, AR, EN")

st.markdown("---")

# 4. Préparation des données pour la chronologie (Timeline)
df_timeline = pd.DataFrame([
    {"Tâche": "Baccalauréat en informatique", "Début": "2010-09-01", "Fin": "2013-06-01", "Catégorie": "Formation"},
    {"Tâche": "Maîtrise : Génie logiciel", "Début": "2013-09-01", "Fin": "2015-06-01", "Catégorie": "Formation"},
    {"Tâche": "Développeuse web & designer (Original Eng.)", "Début": "2015-08-01", "Fin": "2019-04-01", "Catégorie": "Expérience"},
    {"Tâche": "Enseignante (ISET)", "Début": "2016-09-01", "Fin": "2019-07-01", "Catégorie": "Expérience"},
    {"Tâche": "Maîtrise : Multimédia & Web", "Début": "2017-09-01", "Fin": "2020-06-01", "Catégorie": "Formation"},
    {"Tâche": "Agente de voyages (Classy Travel)", "Début": "2024-08-01", "Fin": "2025-02-01", "Catégorie": "Expérience"},
    {"Tâche": "Certificat : Exploitation des données (HEC)", "Début": "2026-01-01", "Fin": "2026-12-31", "Catégorie": "Formation"}
])

# 5. Création de la mise en page
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("🗓️ Chronologie du Parcours")
    fig_timeline = px.timeline(
        df_timeline, 
        x_start="Début", 
        x_end="Fin", 
        y="Tâche", 
        color="Catégorie",
        color_discrete_map={"Formation": "#00A3E0", "Expérience": "#0033A0"},
        template="plotly_white"
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_timeline, width="stretch")

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
        name='Niveau de maîtrise'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        height=400,
        margin=dict(l=40, r=40, t=30, b=30)
    )
    st.plotly_chart(fig_radar, width="stretch")

st.markdown("---")

# 6. Section Certifications et Détails
st.subheader("🏆 Certifications Officielles")
cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.markdown("**Microsoft**")
    st.info("📊 Harnessing the Power of Data with Power BI\n\n📈 Preparing Data for Analysis with Microsoft Excel")

with cert_col2:
    st.markdown("**University of Michigan**")
    st.success("🌐 Building Database Applications in PHP\n\n💻 JavaScript, jQuery, and JSON\n\n📱 Des applications web pour tous")

st.markdown("<br>", unsafe_allow_html=True)
st.button("✉️ Contacter Amani pour une opportunité d'Analyste d'Affaires / Données", width="stretch")