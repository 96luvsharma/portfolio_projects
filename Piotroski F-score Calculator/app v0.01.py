from email.policy import default
import fscore as fs
import bs4
import pandas as pd
import random
import csv
import requests
from io import StringIO
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as si
import streamlit as st

sp500 = fs.sp500()

options = ['Info', 'Calculate']

st.sidebar.title('Options')
app_sidebar = st.sidebar.selectbox('Select an option',options)

st.header(app_sidebar)

if app_sidebar == 'Info':
    st.header("Piotrosky's F-score")
    st.subheader("What is the Piotroski F-Score? ")
    st.write("The Piotroski score is a discrete score between 0-9 that reflects nine criteria used to determine the strength of a firm's financial position. It was originally developed to give investors an idea as to which companies are the strongest when grouped with value stocks. This is done to help highlight the best and worst performers before adding these stocks to a portfolio. The financial strength of the companies is determined by applying these nine accounting-based restrictions and awarding one point for each restriction that a stock passes:")
    st.subheader("A. Profitability")
    st.write("1. Net Income: Give 1 point if Net income  in the current period is positive; otherwise give 0 points.")
    st.write("2. Operating cash flow: Give 1 point if Cash flow from operations in the current period is positive; otherwise give 0 points.")
    st.write("3. Return on assets: Give 1 point if the current period's Return on assets (ROA) is higher when compared to the ROA of the previous period; otherwise give 0 points.")
    st.write("4. Quality of earnings: Give 1 point if the Cash flow from operations exceeds Net income before Extraordinary items; otherwise give 0 points.")
    st.subheader("B. Leverage, Liquidity, and Sources of Funds")
    st.write("1. Decrease in Leverage: Give 1 point if there is a lower ratio of Long term debt in the current period compared to the value in the previous period; otherwise give 0 points.")
    st.write("2. Increase in Liquidity: Give 1 point if the current period's Current ratio is higher when compared to the Current ratio of the previous period; otherwise give 0 points.")
    st.write("3. Absence of Dilution: Give 1 point if the firm did not issue new shares / equity in the preceding period; otherwise give 0 points.")
    st.subheader("C. Operating efficiency")
    st.write("1. Give 1 point if the current period's Gross margin is higher compared to the Gross margin of the previous period; otherwise give 0 points.")
    st.write("2. Asset turnover: Give 1 point if there is a higher Asset turnover ratio period on period (as a measure of productivity); otherwise give 0 points.")
    st.subheader("Meaning")
    st.write("If a company has a score of 8 or 9, it is considered a good value. If the score adds up to between 0-2 points, the stock is considered weak.")



if app_sidebar =='Calculate':

    st.title("Piotroski's F-Score Calculation.")

    selection = st.selectbox("Select the stock you want to analyze", sp500 )


    if len(selection) > 0:
        info_finance = fs.get_statements(selection)
        # Fetch Statements and calculate F-score
        total = fs.total_score(selection)
        profit_score = fs.profitability(selection)
        leverage_score = fs.leverage(selection)
        operating_eff_score = fs.op_eff(selection)
        st.subheader(f'The Total F-score of {selection} = {fs.total_score(selection)}/9')
        st.text(f'The Profitability score for {selection} = {profit_score}/4')
        st.text(f'The Leverage score for {selection} = {leverage_score}/3')
        st.text(f'The Operating Effeciency score for {selection} = {operating_eff_score}/2')
        






