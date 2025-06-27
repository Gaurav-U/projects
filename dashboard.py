import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

st.set_page_config(page_title="Stock Price Dashboard", layout="wide")
st.title("📈 Real-Time Stock Price Dashboard")

symbol = st.text_input("Enter stock ticker (e.g., AAPL, TSLA, TCS.NS):", "AAPL")

data = yf.download(symbol, period="1mo", interval="1d")
st.write(f"Showing data for: {symbol}")
st.dataframe(data.tail())

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="Closing Price", line=dict(color='royalblue', width=2)))
fig.update_layout(title=f"{symbol} Closing Price Over Time", xaxis_title="Date", yaxis_title="Price (USD or INR)")
st.plotly_chart(fig, use_container_width=True)
