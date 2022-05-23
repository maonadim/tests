import streamlit as st
import yfinance as yf
import pandas as pd




st.title("Dashboards Finance")
st.header("oracle capital Dashboard")
st.write("cette application nous aide à analyser les marchés")
st.sidebar.header("Geeksforgeeks \n TrueGeeks")

tickers = ('TSLA','AAPL','MSFT','FB')
dropdown = st.multiselect('Pick your assets',
                          tickers)
start = st.date_input('Start', value=pd.to_datetime('2021-01-01'))
end = st.date_input('Start', value=pd.to_datetime('today'))

if len(dropdown) > 0:
    df = yf.download(dropdown,start,end)['Close']
    st.line_chart(df)
