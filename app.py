import streamlit as st

st.set_page_config(page_title="SimuPro", layout="centered")

st.title("🏦 SimuPro Financement")

# Formulaire principal
with st.container():
    st.subheader("Paramètres du prêt")
    montant = st.number_input("Montant souhaité (€)", value=10000, step=1000)
    duree = st.slider("Durée (années)", 1, 25, 5)
    taux = st.number_input("Taux d'intérêt annuel (%)", value=3.5, step=0.1)
    assurance = st.number_input("Taux assurance annuel (%)", value=0.3, step=0.05)
    age = st.number_input("Âge du client", 18, 80, 35)

# Calculs
duree_mois = duree * 12
taux_mensuel = (taux / 100) / 12
assurance_mensuelle = (montant * (assurance / 100)) / 12

if taux > 0:
    mensualite_pret = (montant * taux_mensuel) / (1 - (1 + taux_mensuel)**(-duree_mois))
else:
    mensualite_pret = montant / duree_mois

total_mensuel = mensualite_pret + assurance_mensuelle
cout_total = (total_mensuel * duree_mois) - montant

# Affichage Pro
st.divider()
st.metric("Mensualité Totale", f"{total_mensuel:,.2f} €")

col1, col2 = st.columns(2)
col1.write(f"**Coût du crédit :** {cout_total:,.2f} €")
col2.write(f"**Âge fin de prêt :** {age + duree} ans")

if age + duree > 75:
    st.error("⚠️ Attention : Limite d'âge dépassée en fin de prêt.")
