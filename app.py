import streamlit as st
import pandas as pd
import datetime

st.title("Konvertor peněz")
list_men = pd.read_csv("physical_currency_list.csv")
list_men_final = list_men["currency code"]
datum = st.date_input("Zadejte datum konverce měny", datetime.date(2023, 5, 7))
datum = datum.strftime('%Y-%m-%d')

col1, col2 = st.columns(2)

with col1:
    mena1 = st.selectbox("Vyber si měnu kterou chceš konvertovat", list_men_final, 142)

with col2:
    castka = st.number_input("Kolik peněz chcete vyměnit", min_value= 0)

mena2 = st.selectbox("Do jaké měny chcete konvertovat", list_men_final, 34)

alpha_outputsize = 'full'
alpha_apikey = 'JCYUNJJG1FH62A97'

btn_konvertovat = st.button("Konvertovat")
if btn_konvertovat:
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={mena1}&to_symbol={mena2}&outputsize={alpha_outputsize}&apikey={alpha_apikey}&datatype=csv'
    tabulka = pd.read_csv(url)
    tabulka = tabulka[["timestamp", "close"]]
    konverzni_datum = max(tabulka[tabulka["timestamp"] < datum]["timestamp"])
    kurz = tabulka.loc[tabulka["timestamp"] == konverzni_datum, "close"].values[0]

    final_castka = kurz*castka
    zaok = round(final_castka, 2)
    
    col3, col4 = st.columns(2)
    
    col3.metric("finalní částka", zaok)

    col4.metric(f"1 {mena1} = ", zaok/castka)

    




