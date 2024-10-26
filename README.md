# 📈 Stock-Trend-Predictor-using-ML

**🌟 Stock Price Predictor: Advanced LSTM Model with RNN**

---

![Stock Predictor](https://img.shields.io/badge/Stock%20Price%20Prediction-LSTM%20Model-blueviolet)
![Python](https://img.shields.io/badge/Made%20with-Python-FFD43B?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Deployed%20with-Streamlit-fuchsia?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔍 **Project Overview**

This repository presents a state-of-the-art **stock price prediction model**, capable of forecasting trends for any stock available on Yahoo Finance. With **Long Short-Term Memory (LSTM)** neural networks at its core, this project embodies a powerful and sophisticated approach to time series forecasting in the fast-paced world of stock markets.

**Model Highlights**:
- **Data Source**: Historical data (20 years) via Yahoo Finance
- **Model Architecture**: Multi-layered LSTM with RNNs, enhanced by dropout for better generalization
- **Performance**: Achieved a Mean Absolute Percentage Error (MAPE) of **7.49%** and R-squared of **0.9317**

---

## 🛠️ **Key Features and Technical Highlights**

### 🔹 **Robust Data Acquisition**  
- Comprehensive historical stock data retrieval using **yfinance**

### 🔹 **Advanced Preprocessing**  
- Implements moving averages, technical indicators, and normalization techniques for clean, reliable data

### 🔹 **Sophisticated LSTM Architecture**  
- Multi-layer LSTM structure with **dropout layers** to enhance prediction accuracy and reduce overfitting

### 🔹 **Adaptive Learning**  
- **Learning rate scheduling** and **early stopping mechanisms** for improved training efficiency and stability

### 🔹 **Comprehensive Visualization**  
- Interactive data visualization tools for easier interpretation of historical data and prediction results

### 🔹 **Streamlit Integration**  
- User-friendly **Streamlit app** enables easy interaction and prediction for any chosen stock

---

## 📊 **Performance Metrics**

| Metric                       | Value  |
|------------------------------|--------|
| **Mean Absolute Error (MAE)**     | 0.0416 |
| **Root Mean Square Error (RMSE)** | 0.0482 |
| **Mean Absolute Percentage Error (MAPE)** | 7.49% |
| **R-squared**                | 0.9317 |

These metrics showcase the model’s **remarkable accuracy** in predicting stock trends, establishing it as a valuable tool for financial analysis and potential use in algorithmic trading strategies.

---

## 💡 **Potential Applications and Adaptability**

While initially optimized for Google stock, this model’s versatile design makes it highly adaptable to various stocks and financial instruments. It serves as an invaluable resource for:
- **Financial Analysts**: Enhances data-driven insights in financial analysis
- **Algorithmic Traders**: Foundation for building sophisticated trading strategies
- **Data Scientists**: Practical, hands-on application of advanced time series forecasting

The project’s modular design supports easy adjustment to new datasets, broadening its potential across diverse financial markets.

---

## 📘 **Educational Value and Ethical Considerations**

This project is intended as an **educational resource**, illustrating the application of deep learning in financial forecasting. It offers a hands-on introduction to **TensorFlow, Keras**, and advanced time series analysis, promoting responsible and well-informed use of machine learning in finance.

> **Disclaimer**: Stock market predictions are inherently uncertain. While the model demonstrates high accuracy, it should not be the sole basis for investment decisions and must be used as a supplement to a comprehensive financial toolkit.

---

## 🚀 **Get Started**

### 🔗 Installation
1. Clone the repository
   ```bash
   git clone https://github.com/username/Stock-Trend-Predictor.git
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

### 📂 **File Structure**
- `data/` - Historical stock data
- `models/` - LSTM model architecture and weights
- `app.py` - Main Streamlit app for interactive predictions
- `README.md` - Project documentation

### 📌 **Requirements**
- Python 3.x
- TensorFlow, Keras, yfinance, Streamlit, matplotlib, pandas, numpy

---

## 🏷️ **License**

[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)  
This project is licensed under the MIT License - see the LICENSE file for details.

---

Happy Predicting! 🎉

