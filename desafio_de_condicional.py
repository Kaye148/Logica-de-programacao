import streamlit as st

st.title("Verificador de idades")

idade = st.number_input("digite sua idade: ", min_value=0, max_value=300, step=1)

if st.button("verificar"):
    if idade < 18:
        st.write("você é menor de idade.")
    else:
        st.write("voê é maior de idade.")

else:
    st.warning("por favor, digite sua idade")
