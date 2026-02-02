import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Cow Calving Monitor", layout="wide")

st.title("🐄 Cow Dry-Off & Calving Monitor")

if "cows" not in st.session_state:
    st.session_state.cows = pd.DataFrame(
        columns=["Cow ID", "Breed", "Age", "Dry Off Date", "Calving Date"]
    )

with st.form("add_cow"):
    cow_id = st.text_input("Cow ID")
    breed = st.text_input("Breed")
    age = st.number_input("Age (years)", min_value=0, step=1)
    dry_off = st.date_input("Dry Off Date")
    calving = st.date_input("Expected Calving Date")
    submit = st.form_submit_button("Add Cow")

    if submit:
        new_row = {
            "Cow ID": cow_id,
            "Breed": breed,
            "Age": age,
            "Dry Off Date": dry_off,
            "Calving Date": calving
        }
        st.session_state.cows = pd.concat(
            [st.session_state.cows, pd.DataFrame([new_row])],
            ignore_index=True
        )
        st.success("Cow added successfully!")

st.subheader("📋 Cow List")
st.dataframe(st.session_state.cows, use_container_width=True)

today = datetime.date.today()
st.subheader("⏰ Calving Alerts")


    (st.session_state.cows["Calving Date"] - today).dt.d_
