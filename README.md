# Developing an Investment Portfolio via Chatbot

<img align="middle" width="850" height="500" src="https://img.freepik.com/free-vector/isometric-chatbot-flowchart-with-smartphones-computers-message-bubbles_1284-55214.jpg?w=1380&t=st=1672885485~exp=1672886085~hmac=3564b76784e0d8b531dadd28cc459a78dfa87f3d220b8b46af532c9ec4f4a0a5">


## Run the Chatbot using Streamlit Cloud:

Link to Chatbot --> https://investachat.streamlit.app/

## Running the Chatbot Locally:
You must download the following packages in order to run the Chatbot:

<span style="color:white;font-weight:100;font-size:15px">
    <b>Python (version 3.9.12):</b>
</span>

    pip install python==3.9.12

<span style="color:white;font-weight:100;font-size:15px">
    <b>Streamlit-Chat Package (version 0.0.2.1):</b>
</span>

    pip install streamlit-chat
    from streamlit_chat import message

<span style="color:white;font-weight:100;font-size:15px">
    <b>Streamlit Package (version 1.15.2):</b>
</span>

    pip install streamlit
    conda install -c conda-forge streamlit
    import streamlit as st

<span style="color:white;font-weight:100;font-size:15px">
    <b>Plotly Package (version 5.9.0):</b>
</span>

    pip install plotly
    conda install -c plotly plotly
    import plotly.express as px
    import plotly.graph_objects as go

---

<p align="center">
  <img src="./Images/Project_Roadmap.png"/>
</p>

> Note:
> Our team was interested in expanding our previous project:
[Developing an Investment Portfolio Utilizing Machine Learning](https://github.com/Mun-Min/Project_Two)

## Summary:

<span style="color:white;font-weight:100;font-size:15px">
    <b>A:</b>
</span>

* According to the Rule of 110, the percentage of your retirement portfolio that should be invested in stocks should be calculated by subtracting your age from 110. For instance, if you are 30, this rule suggests that you should allocate 80% of your portfolio to stocks and the rest to other non-stock investments. However, some current investment advice recommends including a small portion, ranging from 1-5%, of cryptocurrency investments in a retirement portfolio. The rest of the portfolio should be divided between investments in bonds and real estate investment trusts (REITs).
  
  * To enhance our project, we have decided to add in Bitcoin and Ethereum, which are the two largest cryptocurrencies in terms of market cap.
  * Assets chosen to be included in portfolio:

    * Top 25 SP500 Stocks (ranked by marketcap)
    * 10-yr Treasury Bond, 30-yr Treasury Bond
    * Bitcoin, Ethereum

<span style="color:white;font-weight:100;font-size:15px">
    <b>B:</b>
</span>

* Utilize FaceBook's Prophet Forecasting ML Model to forecast adjusted close prices of each asset for the next 30 days.

<span style="color:white;font-weight:100;font-size:15px">
    <b>C:</b>
</span>

* Run Monte Carlo Simulations to also include long-term projections to furthur analyze the portfolio.

## Data Techniques:

Data Sources: Yahoo Finance Python Package

* Stocks [Top 25 SP500]
* Bonds [10 yr & 30 yr Treasury Yield]
* Crypto [BTC & ETH]

Gathered 10 years of Historical Data

## Chatbot Development:
