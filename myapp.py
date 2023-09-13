import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
         ## Простое приложение для определения цен на акции
Показаны цена закрытия акций и объем продаж Apple!
         """)
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2023-9-11')

st.write("""
         ### Цена закрытия
         """)
st.line_chart(tickerDf.Close)

st.write("""
         ### Объем продаж
         """)
st.line_chart(tickerDf.Volume)



