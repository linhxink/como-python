import streamlit as st 

tvar = st.radio("vyber si tvar", ["ctverec", "obdelnik", "kružnice"])

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
    
st.header ("Moje aplikace")
