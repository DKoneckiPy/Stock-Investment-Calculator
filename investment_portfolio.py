

##Code
"""

#library import

import pandas as pd 
import pandas_datareader as pdr
import datetime as dt
import numpy as np

import matplotlib.pyplot as plt

#Portfolio stocks dataframe
#If you want to abort adding companies, enter 'END' ticker 
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

test = pd.DataFrame(columns=['Stocks','Capital','BuyPrice','LastPrice','Profit(%)','Profit(zł)'])

while True:
  ticker =  input("Enter the ticker name:")
  ticker2 = ticker + ".pl" 
  if ticker == 'END' :
    break
  df = pdr.get_data_stooq(ticker2,start=dt.datetime(2015,1,1))
  invdate = input('Enter the date of purchase of the shares (RRRR-MM-DD):')
  firstprice2 = df.loc[invdate].iloc[0][0]
  lastprice = df['Close'].iloc[0]
  list3.append(lastprice)
  list1.append(ticker2)
  list4.append(firstprice2)
  lots = int(input('Enter the amount of invested capital:'))
  list2.append(lots)
  profit_pct = round(((lastprice - firstprice2)/firstprice2)*100,2)
  list5.append(profit_pct)
  finalcapital = round((1+(((lastprice-firstprice2))/firstprice2))*lots,2)
  list7.append(finalcapital)
  profit_zl = round(finalcapital-lots,2)
  list6.append(profit_zl) 
  
portfolio = pd.DataFrame(columns=['Stocks','BuyCapital','BuyPrice','LastPrice','Profit(%)','Profit(zł)','FinalCapital'])
portfolio['Stocks'] = list1
portfolio['BuyCapital'] = list2
portfolio['BuyPrice'] = list4
portfolio['LastPrice'] = list3
portfolio['Profit(%)'] = list5
portfolio['Profit(zł)'] = list6
portfolio['FinalCapital'] = list7

BuyCapital = portfolio['BuyCapital'].sum()
Profit_prc = (portfolio['FinalCapital'].sum()-portfolio['BuyCapital'].sum())/ portfolio['BuyCapital'].sum()*100
Profit_zl = portfolio['FinalCapital'].sum()- portfolio['BuyCapital'].sum()
FinalCapital= portfolio['FinalCapital'].sum()
portfolio.loc['TOTAL'] = ['-',BuyCapital,'-','-',Profit_prc,Profit_zl,FinalCapital]


portfolio

