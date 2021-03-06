# Finance related Projects I've been working on

> Currently working on DCF analysis

My working Finance projects to showcase my skills and knowledge

# 1. Piotrosky's F-Score Calculation App.
This Python code fetches the financial statements from Yahoo_Finance and interprets values like Gross Margin, Current Ratio, Operating Effeciency
based on Piotrosky's F-score model, and then gives any company you select  a score out of 9.

#### Here's a representation of how the model works, for detailed info you can see my Python code here in the repository.
![](img/Fscore.gif)

As the models are already created we just need to change "AAPL" with the ticker symbol of the required company

# 2. Apple Stock Price Prediction - It uses LSTM(Long Short Term Memory) model to predict the price of stock one day in advance.
![](vid/Piotroskiscore_app.webm)

The orange line shows the actual price and the yellow one is the predicted price, the blue line is the data used to train the model.

### The Root Mean Squared Error(RMSE) was = 1.6542070345445112 
![](img/pred_aaplc.png)
###### I learnt this method through youtube channel called [Computer Science](https://www.youtube.com/c/ComputerSciencecompsci112358)

# On 8th March, 2022:
## The predicted price of the AAPL is = 160.47377
## The actual price of the AAPL is = 157.440002


# 3. Financial Ratios Analysis. 

Here are some examples of the Financial Ratios Analysis done in python, 
Python makes it very easy to practically retrieve any financial ratio of any company within minutes for any company,
I also use an api from **[Financial Modelling Prep](https://site.financialmodelingprep.com/developer/docs)** which makes things even easier.

Here are the Quick Ratio, ROE and Debt Ratio for AAPL for the past five years
##### Where 0 is now and 4 is five years in the past.
![](img/finratios_1.png)

Another ratio analysis for AAPL.
![](img/finratios_2.png)
