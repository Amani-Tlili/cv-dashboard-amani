import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import base64
from PIL import Image

# 1. Configuration de la page
st.set_page_config(page_title="Amani Tlili - Resume Dashboard", layout="wide", initial_sidebar_state="collapsed")

# 2. Injection de CSS 
st.markdown("""
<style>
    /* Fond de l'application (Lavande clair) */
    .stApp {
        background-color: #E8E7FB;
    }
    
    /* Conteneur principal */
    .block-container {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 2rem 3rem !important;
        margin-top: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        max-width: 1300px;
    }

    /* Typographie */
    h1, h2, h3, h4, p, span, div {
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Bouton Pilule pour le nom */
    .name-pill {
        background: linear-gradient(90deg, #9a88cf 0%, #FF7F50 100%);
        color: white;
        text-align: center;
        padding: 12px;
        border-radius: 30px;
        font-size: 22px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    /* Titre du poste */
    .job-title {
        text-align: center;
        font-size: 16px;
        color: #666666;
        margin-bottom: 20px;
    }

    /* Lignes de séparation discrètes */
    hr {
        border-top: 1px solid #e0e0e0;
        margin: 20px 0;
    }

    /* Formatage des listes */
    .cv-entry {
        display: flex;
        margin-bottom: 15px;
    }
    .cv-year {
        min-width: 90px;
        font-weight: bold;
        color: #9a88cf;
        font-size: 14px;
    }
    .cv-details {
        flex-grow: 1;
        font-size: 14px;
    }
    .cv-role {
        font-weight: bold;
        color: #333333;
    }
    .cv-company {
        color: #666666;
        font-size: 13px;
    }

    /* Barres de progression HTML personnalisées */
    .skill-container {
        margin-bottom: 15px;
    }
    .skill-label {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .progress-bg {
        background-color: #FBE8F1; /* Rose poudré */
        border-radius: 10px;
        height: 12px;
        width: 100%;
        position: relative;
    }
    .progress-bar {
        background: linear-gradient(90deg, #9a88cf 0%, #FF7F50 100%); /* Violet vers Corail */
        height: 100%;
        border-radius: 10px;
    }
    
    /* Arrondir la photo de profil */
    [data-testid="stImage"] img {
        border-radius: 50%;
        border: 6px solid #FBE8F1;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* Liens personnalisés */
    .custom-link {
        text-decoration: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .custom-link:hover {
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

# Définition de la fonction pour dessiner les barres de progression
def draw_skill(skill_name, percentage):
    return f"""
    <div class='skill-container'>
        <div class='skill-label'>{skill_name}</div>
        <div class='progress-bg'>
            <div class='progress-bar' style='width: {percentage}%;'></div>
        </div>
    </div>
    """

# 3. Structure en 3 colonnes 
col_left, col_mid, col_right = st.columns([1, 2, 1], gap="large")

# ==========================================
# COLONNE DE GAUCHE : PROFIL
# ==========================================
with col_left:
    if os.path.exists("photo_profil.jpg"):
        img = Image.open("photo_profil.jpg")
        st.image(img, use_container_width=True)
    else:
        st.markdown("<div style='height: 200px; width: 200px; background-color:#e0e0e0; border-radius:50%; margin:auto; line-height:200px; text-align:center;'>Photo</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='name-pill'>AMANI TLILI</div>", unsafe_allow_html=True)
    st.markdown("<div class='job-title'>Analyste de Données & Affaires</div>", unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center; font-size: 14.5px;'>", unsafe_allow_html=True)
    st.markdown("**Téléphone**<br>📞 (438) 855-1310", unsafe_allow_html=True)
    st.markdown("<br>**Email**<br>✉️ ameni1tlili@gmail.com", unsafe_allow_html=True)
    st.markdown("<br>**LinkedIn**<br>🔗 <a href='https://www.linkedin.com/in/amanitlili/' target='_blank' class='custom-link' style='color: #9a88cf;'>/in/amanitlili</a>", unsafe_allow_html=True)
    st.markdown("<br>**Portfolio**<br>🌐 <a href='https://amani-tlili.github.io/amanitlili-portfolio/index.html' target='_blank' class='custom-link' style='color: #FF7F50;'>Voir mon Portfolio</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    cv_file_path = "Amani_Tlili_CV_Spontanee_Final.pdf"
    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            st.download_button("📥 Télécharger CV (PDF)", data=pdf_file, file_name="Amani_Tlili_CV.pdf", mime="application/pdf", use_container_width=True)

# ==========================================
# COLONNE DU MILIEU : PARCOURS & LANGUES
# ==========================================
with col_mid:
    st.markdown("### About Me")
    st.markdown("""
    <p style='text-align: justify; font-size: 14.5px;'>
    Étudiante au certificat en exploitation des données à HEC Montréal et titulaire de deux maîtrises en informatique[cite: 1]. Je possède une solide base en développement logiciel, en méthodologies Agiles et en analyse de données (SQL, Python, ETL)[cite: 1]. Possédant une expérience concrète dans la collecte de besoins d'affaires, la modélisation de bases de données et la documentation technique, je souhaite mettre mes compétences au service d'initiatives technologiques visant à optimiser les processus[cite: 1].
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col_work, col_edu = st.columns(2)
    
    with col_work:
        st.markdown("### Work Experience")
        work_html = """
        <div class='cv-entry'><div class='cv-year'>2024 - 2025</div><div class='cv-details'><span class='cv-role'>Agente de voyages</span><br><span class='cv-company'>Classy Travel - Montréal, QC</span></div></div>
        <div class='cv-entry'><div class='cv-year'>2016 - 2019</div><div class='cv-details'><span class='cv-role'>Enseignante</span><br><span class='cv-company'>ISET - Tunisie</span></div></div>
        <div class='cv-entry'><div class='cv-year'>2015 - 2019</div><div class='cv-details'><span class='cv-role'>Développeuse web & designer</span><br><span class='cv-company'>Original Engineering - Tunisie</span></div></div>
        """
        st.markdown(work_html, unsafe_allow_html=True)
        
    with col_edu:
        st.markdown("### Education")
        edu_html = """
        <div class='cv-entry'><div class='cv-year'>2026 - Prsnt</div><div class='cv-details'><span class='cv-role'>Certificat en données</span><br><span class='cv-company'>HEC Montréal</span></div></div>
        <div class='cv-entry'><div class='cv-year'>2017 - 2020</div><div class='cv-details'><span class='cv-role'>Maîtrise Multimédia</span><br><span class='cv-company'>Institut Sup. d'Informatique</span></div></div>
        <div class='cv-entry'><div class='cv-year'>2013 - 2015</div><div class='cv-details'><span class='cv-role'>Maîtrise Génie Logiciel</span><br><span class='cv-company'>ISET</span></div></div>
        <div class='cv-entry'><div class='cv-year'>2010 - 2013</div><div class='cv-details'><span class='cv-role'>Baccalauréat Informatique</span><br><span class='cv-company'>ISET</span></div></div>
        """
        st.markdown(edu_html, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Nouvelle section Langues sous forme de barres
    st.markdown("### Languages")
    col_lang1, col_lang2 = st.columns(2)
    
    with col_lang1:
        st.markdown(draw_skill("🇹🇳 Arabe (Bilingue)", 100), unsafe_allow_html=True)
        st.markdown(draw_skill("🇬🇧 Anglais (Intermédiaire)", 60), unsafe_allow_html=True)
    with col_lang2:
        st.markdown(draw_skill("🇫🇷 Français (Courant)", 95), unsafe_allow_html=True)

# ==========================================
# COLONNE DE DROITE : COMPÉTENCES & GRAPHIQUES
# ==========================================
with col_right:
    st.markdown("### Skills")
    
    skills_html = draw_skill("Power BI & GA4", 95)
    skills_html += draw_skill("SQL & Modélisation", 90)
    skills_html += draw_skill("Analyse d'Affaires & UML", 90)
    skills_html += draw_skill("Python (Pandas, ETL)", 85)
    skills_html += draw_skill("Méthodologies Agiles", 85)
    
    st.markdown(skills_html, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col_kpi, col_chart = st.columns([1, 1])
    
    with col_kpi:
        st.markdown("<div style='color:#9a88cf; font-size:35px; font-weight:bold; margin-top:20px;'>5</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:12px; line-height:1.2; margin-bottom:15px;'>Certifications<br>Officielles</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='color:#FF7F50; font-size:35px; font-weight:bold;'>3</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:12px; line-height:1.2;'>Diplômes<br>Universitaires</div>", unsafe_allow_html=True)
        
    with col_chart:
        # Ajout de textinfo='none' pour cacher les pourcentages noirs qui débordaient
        fig1 = go.Figure(data=[go.Pie(labels=['Dev', 'Data'], values=[60, 40], hole=.75, marker_colors=['#9a88cf', '#e0e0e0'], textinfo='none', hoverinfo='label')])
        fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=80, paper_bgcolor="rgba(0,0,0,0)", annotations=[dict(text='IT', x=0.5, y=0.5, font_size=14, showarrow=False)])
        st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})
        
        fig2 = go.Figure(data=[go.Pie(labels=['Data', 'Autre'], values=[85, 15], hole=.75, marker_colors=['#FF7F50', '#e0e0e0'], textinfo='none', hoverinfo='label')])
        fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=80, paper_bgcolor="rgba(0,0,0,0)", annotations=[dict(text='Data', x=0.5, y=0.5, font_size=14, showarrow=False)])
        st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
