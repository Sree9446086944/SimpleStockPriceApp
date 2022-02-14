import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Stock Price App

Shows are the stock **closing price** and ***volume*** line charts of the company entered.
""")
name = st.text_input("Enter ticker symbol", "")

def stock(result):
    #define the ticker symbol
    tickerSymbol = result  # AAPL FOR Apple

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    print(yf.Ticker(tickerSymbol).info['longName'])
    st.write(yf.Ticker(tickerSymbol).info['longName'])

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2022-2-1')

    st.write("""
    ## Closing Price 

    """)
    st.line_chart(tickerDf.Close)
    st.write("""
    ## Volume
    """)
    st.line_chart(tickerDf.Volume)
 
# display the line charts after Submit button clicked
if(st.button('Submit')):
    result = name.title().upper()
    print(result)
    #define the function before the call
    stock(result)

