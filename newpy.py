import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go


st.set_page_config(page_title="Stock Trend Predictor", page_icon="📈", layout="wide")


st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        color: #1E88E5;
    }
    .stApp {
        background-color: #F0F8FF;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<p class="big-font">Stock Trend Predictor</p>', unsafe_allow_html=True)


with st.sidebar:
    st.header("Configuration")
    stock = st.text_input("Enter the Stock Symbol", "GOOG")
    years = st.slider("Years of historical data", 1, 20, 10)
    
    
    predict_button = st.button("Predict Trends")


col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Stock Data")
    
    
    end = datetime.now()
    start = end - timedelta(days=years*365)
    
    
    @st.cache_data
    def load_data(symbol, start, end):
        return yf.download(symbol, start, end)
    
    data_load_state = st.text('Loading data...')
    stock_data = load_data(stock, start, end)
    data_load_state.text('Loading data... done!')

    
    st.dataframe(stock_data.style.highlight_max(axis=0))

with col2:
    st.subheader("Stock Info")
    ticker = yf.Ticker(stock)
    info = ticker.info
    
    if 'logo_url' in info and info['logo_url']:
        st.image(info['logo_url'], width=100)
    
    st.write(f"**{info.get('longName', stock)}**")
    st.write(f"Sector: {info.get('sector', 'N/A')}")
    st.write(f"Industry: {info.get('industry', 'N/A')}")
    
    if 'currentPrice' in info and 'regularMarketChangePercent' in info:
        st.metric("Current Price", f"${info['currentPrice']:.2f}", f"{info['regularMarketChangePercent']:.2f}%")
    else:
        st.write("Current price information not available")


st.subheader("Stock Price Trend")
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name="Close Price"))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].rolling(100).mean(), name="100-day MA"))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'].rolling(250).mean(), name="250-day MA"))
fig.update_layout(title=f"{stock} Stock Price", xaxis_title="Date", yaxis_title="Price", legend_title="Indicators")
st.plotly_chart(fig, use_container_width=True)


if predict_button:
    st.subheader("Price Prediction")
    
    
    model = load_model(r"C:\Users\aksha\OneDrive\Desktop\NIF50\SSD1F.keras")
    
    
    splitting_len = int(len(stock_data)*0.7)
    x_test = pd.DataFrame(stock_data.Close[splitting_len:])
    
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(x_test[['Close']])
    
    x_data = []
    y_data = []
    
    for i in range(100, len(scaled_data)):
        x_data.append(scaled_data[i-100:i])
        y_data.append(scaled_data[i])
    
    x_data, y_data = np.array(x_data), np.array(y_data)
    
    
    predictions = model.predict(x_data)
    inv_pre = scaler.inverse_transform(predictions)
    inv_y_test = scaler.inverse_transform(y_data)
    
    plotting_data = pd.DataFrame(
        {
            'Original': inv_y_test.reshape(-1),
            'Predicted': inv_pre.reshape(-1)
        },
        index = stock_data.index[splitting_len+100:]
    )
    
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=plotting_data.index, y=plotting_data['Original'], name="Actual Price"))
    fig.add_trace(go.Scatter(x=plotting_data.index, y=plotting_data['Predicted'], name="Predicted Price"))
    fig.update_layout(title="Actual vs Predicted Stock Price", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig, use_container_width=True)

    
    mape = np.mean(np.abs((plotting_data['Original'] - plotting_data['Predicted']) / plotting_data['Original'])) * 100
    st.metric("Prediction Accuracy", f"{100-mape:.2f}%")


st.markdown("---")
st.markdown("Created with ❤️ by Akshat")