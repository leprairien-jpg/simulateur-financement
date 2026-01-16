import streamlit as st

# 1. FORCE LE NOM ET L'ICÔNE DANS LE NAVIGATEUR
st.set_page_config(
    page_title="EXPERT FINANCEMENT", 
    page_icon="💰", 
    layout="centered"
)

# 2. LE BRISEUR DE CACHE (Script pour forcer Android à oublier "Streamlit")
st.markdown("""
    <script>
        // Change le titre que Chrome utilise pour l'icône
        window.parent.document.title = "EXPERT FINANCES";
        
        // Supprime les anciens réglages de l'application dans le navigateur
        if ('serviceWorker' in navigator) {
          navigator.serviceWorker.getRegistrations().then(function(registrations) {
            for(let registration of registrations) {
              registration.unregister();
            }
          });
        }
    </script>
    <style>
        /* Change la couleur de la barre du haut pour prouver que c'est une nouvelle version */
        header[data-testid="stHeader"] {
            background-color: #1a1a1a !important;
        }
        .main {
            background-color: #f0f2f6;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. TON APPLICATION PRO
st.title("🏦 SimuPro Expert")
st.write("---")

# Formulaire
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        montant = st.number_input("Montant (€)", value=15000, step=1000)
        duree = st.slider("Durée (années)", 1, 30, 10)
    with col2:
        taux = st.number_input("Taux (%)", value=3.5, step=0.1)
        assurance = st.number_input("Assurance (%)", value=0.30, step=0.05)
        age = st.number_input("Âge du client", 18, 85, 30)

# Calculs simples
duree_m = duree * 12
t_m = (taux / 100) / 12
if taux > 0:
    m_hors = (montant * t_m) / (1 - (1 + t_m)**(-duree_m))
else:
    m_hors = montant / duree_m
m_ass = (montant * (assurance / 100)) / 12
m_totale = m_hors + m_ass

# Affichage
st.divider()
st.metric("Mensualité Totale", f"{m_totale:,.2f} €")
st.info(f"Fin de prêt à : {age + duree} ans")
