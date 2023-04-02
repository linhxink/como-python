import streamlit as st 

st.header ("Moje aplikace") 

tvar = st.radio("vyber si tvar", ["ctverec", "obdelnik", "kružnice", "krychle", "kvádr"])

if tvar == "ctverec":
    strana = st.number_input("zadejte stranu ctverce")
    st.text(f"obvod ctverce je {strana*4} a obsah je {strana**2}")

elif tvar == "obdelnik":
    strana_a = st.number_input("zadejte stranu a: ")
    strana_b = st.number_input("zadejte stranu b: ")
    st.text(f"obvod je {2*strana_a + 2*strana_b} a obsah {strana_b*strana_a}")

elif tvar == "kružnice": 
    polomer = st.number_input("zadejte polomer kruznice")
    st.text(f"obvod kružnice je {2*3.14*polomer} a obsah {3.14*polomer**2}")
    
elif tvar == "krychle":
    strana_krychle = st.number_input("zadejte stranu krychle")
    st.text(f"povrch krychle je {6*strana_krychle**2} a objem je {strana_krychle**3}")

elif tvar == "kvádr":
    strana_kvadru = st.number_input("zadejte stranu a")
    strana_kvadru2 = st.number_input("zadejte stranu b")
    strana_kvadru3 = st.number_input("zadejte stranu c")
    st.text(f"povrch kvadru je {2*(strana_kvadru*strana_kvadru2+strana_kvadru*strana_kvadru3+strana_kvadru2*strana_kvadru3)} a objem je {strana_kvadru*strana_kvadru2*strana_kvadru3}")
    