import streamlit as st

# 1. Configuration de la page (Nom et Icône dans le navigateur)
st.set_page_config(
    page_title="SimuPro Financement", 
    page_icon="💰", 
    layout="centered"
)

# Style CSS pour un rendu plus pro et compact sur mobile
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 SimuPro Financement")
st.write("Outil professionnel de simulation de crédit")

# --- SECTION PARAMÈTRES ---
with st.expander("⚙️ Paramètres du prêt", expanded=True):
    col_a, col_b = st.columns(2)
    
    with col_a:
        montant = st.number_input("Montant du prêt (€)", value=20000, step=1000)
        duree_ans = st.slider("Durée (années)", 1, 30, 15)
        age = st.number_input("Âge du client", 18, 85, 35)

    with col_b:
        taux_annuel = st.number_input("Taux d'intérêt (%)", value=3.50, step=0.1, format="%.2f")
        taux_assurance = st.number_input("Taux assurance (%)", value=0.30, step=0.05, format="%.2f")

# --- CALCULS ---
duree_mois = duree_ans * 12
taux_mensuel = (taux_annuel / 100) / 12

# Calcul mensualité crédit
if taux_annuel > 0:
    mensualite_hors_assurance = (montant * taux_mensuel) / (1 - (1 + taux_mensuel)**(-duree_mois))
else:
    mensualite_hors_assurance = montant / duree_mois

# Calcul assurance
mensualite_assurance = (montant * (taux_assurance / 100)) / 12
mensualite_totale = mensualite_hors_assurance + mensualite_assurance
cout_total_interets = (mensualite_hors_assurance * duree_mois) - montant
cout_total_assurance = mensualite_assurance * duree_mois
total_paye = montant + cout_total_interets + cout_total_assurance

# --- AFFICHAGE DES RÉSULTATS ---
st.subheader("📊 Résultats")

c1, c2 = st.columns(2)
with c1:
    st.metric("Mensualité Totale", f"{mensualite_totale:,.2f} €")
    st.write(f"**Dont assurance :** {mensualite_assurance:,.2f} €")

with c2:
    st.metric("Coût Total Crédit", f"{cout_total_interets + cout_total_assurance:,.2f} €")
    st.write(f"**Âge fin de prêt :** {age + duree_ans} ans")

# Alertes de sécurité
if age + duree_ans > 75:
    st.error(f"⚠️ Attention : Le client aura {age + duree_ans} ans à l'échéance.")

# --- RÉCAPITULATIF PRO ---
st.divider()
with st.expander("🔍 Détails du financement"):
    st.write(f"**Capital emprunté :** {montant:,.0f} €")
    st.write(f"**Total des intérêts :** {cout_total_interets:,.2f} €")
    st.write(f"**Total des assurances :** {cout_total_assurance:,.2f} €")
    st.info(f"**Montant total remboursé :** {total_paye:,.2f} €")
