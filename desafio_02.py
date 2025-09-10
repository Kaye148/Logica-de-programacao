# verificando a média 
# solicite ao usúario a média do aluno 
# se maior os igual a 7,mostre como aprovado
# caso contrario, moste como reprovado

import streamlit as st

st.title ("vercificador de aprovação")

media = st.number_input("digite sua média: ",step=3)

if st.button ("virificar média"):
     if media <= 6.9:
          st.error("você foi reprovado")
          
     else:
          st.success("você foi aprovado")

else:
     st.info("por favor informe a média.")

# success - verde
# warning - amarelo
# info - azul
# error - vermelho 




