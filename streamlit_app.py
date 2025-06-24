import streamlit as st

# Titre du site
st.title("Prédiction de scores exacts ⚽")

# Scores précédents (exemple simple)
previous_scores = [(2, 1), (1, 0), (3, 2), (0, 1), (2, 2)]

st.subheader("Scores précédents")
st.write(previous_scores)

# Calcul de la moyenne des scores
home_avg = sum(score[0] for score in previous_scores) / len(previous_scores)
away_avg = sum(score[1] for score in previous_scores) / len(previous_scores)

# Affichage de la prédiction simple
st.subheader("Prédiction basée sur la moyenne :")
st.write(f"{home_avg:.1f} - {away_avg:.1f}")
