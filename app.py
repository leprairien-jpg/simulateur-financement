import streamlit as st

# 1. CONFIGURATION DE BASE
st.set_page_config(
    page_title="FINANCEMENT PRO", 
    page_icon="💰", 
    layout="centered"
)

# 2. INJECTION POUR FORCER CHROME (Le "Forceur")
# Ce code change le titre de l'onglet et l'icône pour que Chrome ne les confonde plus
st.markdown(f"""
    <script>
        var link = document.querySelector("link[rel*='icon']") || document.createElement('link');
        link.type = 'image/x-icon';
        link.rel = 'shortcut icon';
        link.href = 'https://cdn-icons-png.flaticon.com/512/2845/2845874.png';
        document.getElementsByTagName('head')[0].appendChild(link);
        window.parent.document.title = "FINANCEMENT PRO";
    </script>
    """, unsafe_allow_html=True)

# 3. STYLE VISUEL PERSONNALISÉ
st.markdown("""
    <style>
    /* Change la couleur de la barre du haut pour la différencier */
    header[data-testid="stHeader"] {
        background-color: #002b36;
    }
    .main {
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. CONTENU DE L'APPLICATION
st.title("🏦 Simulateur Expert")
st.write("---")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        montant = st.number_input("Montant (€)", value=25000, step=1000)
        duree = st.slider("Durée (ans)", 1, 30, 15)
    with col2:
        taux = st.number_input("Taux d'intérêt (%)", value=3.5, step=0.1)
        assurance = st.number_input("Assurance (%)", value=0.35, step=0.05)
        age = st.number_input("Âge actuel", 18, 80, 35)

# Calculs
duree_m = duree * 12
t_mensuel = (taux / 100) / 12
mensu_hors_ass = (montant * t_mensuel) / (1 - (1 + t_mensuel)**(-duree_m)) if taux > 0 else montant/duree_m
mensu_ass = (montant * (assurance / 100)) / 12
mensu_totale = mensu_hors_ass + mensu_ass

# Affichage des résultats
st.divider()
st.metric("Mensualité Totale", f"{mensu_totale:,.2f} €")

if age + duree > 75:
    st.error(f"⚠️ Risque : Fin de prêt à {age + duree} ans.")
else:
    st.success(f"Âge fin de prêt : {age + duree} ans.")
