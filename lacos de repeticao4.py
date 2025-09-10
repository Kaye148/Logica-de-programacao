import streamlit as st
import time
st.title("Laços de Repetição - FOR")
 
st.header("contagem de 1 a 10.")


numero = st.number_input("digite até onde quer o laço de repetição:", step=1)

if st.button("iniciar"):
    for i in range(1,numero+1, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")
