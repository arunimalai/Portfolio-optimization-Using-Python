# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:51:40 2026

@author: HP
"""

import pandas as pd
#%%
import numpy as np
#%%
import matplotlib.pyplot as plt
#%%


# LIST THE FOUR STOCK TICKER SYMBOLS FOR OUR PORTFOLIO

stock_list=['AMD','AAPL','MSFT','ORCL']

# Create an empty dictionary to store our stock info

stocks={}

# Loop through each stock in the stock_list

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "main"

for i_stock in stock_list:
    stocks[i_stock] = pd.read_csv(
        DATA_DIR / f"{i_stock}.csv",
        parse_dates=True,
        index_col="Date")
#%%

# create 'normalised return' column for each stock

for stock_name, stock_data in stocks.items():
    first_adj_close = stock_data.iloc[0]['Adj Close']
    stock_data['Normalized Return'] = stock_data['Adj Close']/first_adj_close
#%%
stocks['AAPL'].head()
#%%

# Create Allocation for each stock - equally weighted in our portfolio

for stock_name, stock_data in stocks.items():
    stock_data['Allocation'] = stock_data['Normalized Return']*0.25

stocks['AAPL'].head()
#%%

#Set the value of the portfolio to $10k

for stock_name, stock_data in stocks.items():
    stock_data['Position Value'] = stock_data['Allocation']*10000

stocks['AMD'].head()

#%%

# create Position Values dictionary

position_values = {}

for stock_name,stock_data in stocks.items():
    position_values[stock_name] = stock_data['Position Value']

#%%

# Convert the Position Values Dictionary to a Dataframe

position_values = pd.DataFrame(data=position_values)

position_values.head()

#%%

# Add "Total" Column to position values, summing the other columns

position_values['Total'] = position_values.sum(axis = 1)

position_values.head()

#%%

# View the Total Portfolio

plt.figure(figsize=(12,8))
plt.plot(position_values['Total'])
plt.title('Equal-Weighted Portfolio Performance')
plt.ylabel('Total Value')

#%%

# View the four stocks in Portfolio

plt.figure(figsize=(12,8))
plt.plot(position_values.iloc[:,0:4])
plt.title('Equal-Weighted Portfolio Stock Performance')
plt.ylabel('Total Value')

#%%

# Define the end and start value of the portfolio

end_value = position_values['Total'].iloc[-1]
start_value = position_values['Total'].iloc[0]

# Calculate the cumulative portfolio return as percentage

cumulative_return = end_value/start_value - 1

print(cumulative_return)

#%%

# create a 'daily returns' column

position_values['Daily Returns'] = position_values['Total'].pct_change()

position_values.head()

#%%

# calculate mean daily return

mean_daily_return = position_values['Daily Returns'].mean()

print('The mean daily return is : ', str(mean_daily_return))

#%%

# Calculate the standard deviation of Daily Return

stdev_daily_return = position_values['Daily Returns'].std()

print('The standard deviation of daily return is : ', str(stdev_daily_return))

#%%
'''SHARPE RATIO- It is a risk adjusted return metric that helps to quantify 
how much return we are getting for a given level of risk. Calculated as average 
return of portfolio minus risk-free rate, divided by std deviation of the return'''   

# Calculate the Sharpe Ratio:
    
sharpe_ratio = mean_daily_return/stdev_daily_return

print(str(sharpe_ratio))

# Calculate annualised Sharpe Ratio

sharpe_ratio_annualised = sharpe_ratio*252**0.5

print(str(sharpe_ratio_annualised))

#%%

''' OPTIMISED PORTFOLIO WEIGHTING'''

# Create stock_adj_close dictionary

stock_adj_close = {}

for stock_name, stock_data in stocks.items ():
    stock_adj_close[stock_name] = stock_data['Adj Close']

stock_adj_close = pd.DataFrame(data=stock_adj_close)

stock_adj_close.head()

#%%

# Create stock_returns DataFrames to see the day over any change in stock value

stock_returns = stock_adj_close.pct_change()

stock_returns.head()
#%%
'''Define the number of scenarios and create a blank array to populate stock
weightings for each scenario'''

scenarios = 10000

weights_array =  np.zeros((scenarios, len(stock_returns.columns)))

weights_array

#%%

# Create additional blank arrays for scenario output

returns_array = np.zeros(scenarios)
volatility_array = np.zeros(scenarios)
sharpe_array = np.zeros(scenarios)

#%%

# Import the random package and set the seeds

import random
random.seed(3)
np.random.seed(3)
 
for index in range(scenarios):
    
# Generate four random numbers for each index 

    numbers = np.array(np.random.random(4))

# Divide each number by the sum of the numbers to generate the random weight

    weights = numbers/np.sum(numbers)

#save the weights in weights_array   
    weights_array[index,:] = weights
    
#Calculate the return for each scenario
    returns_array[index] = np.sum(stock_returns.mean()*252*weights)
    
#Calculate the expected Volatility for each scenario
    volatility_array[index] = np.sqrt(np.dot(weights.T,np.dot(stock_returns.cov()*252,weights)))

#Calculate the Sharpe Ratio for each Scenario
    sharpe_array[index] = returns_array[index] / volatility_array[index]
    
print('The first combination:', weights_array[0])
#%%
print('The Sharpe ratio of the first portfolio:', sharpe_array[0])
#%%

'''IDENTIFY THE OPTIMAL PORTFOLIO'''

# Find the highest Sharpe Ratio in sharpe_array

sharpe_array.max()

#Find the index of the Optimal Portfolio

index_max_sharpe = np.argmax(sharpe_array)
str(index_max_sharpe)

optimal_weights = weights_array[index_max_sharpe, :]

optimal_portfolio = pd.DataFrame({ 'Stock': stock_list, 'Weight': optimal_weights})

optimal_portfolio.to_csv( 'results/optimal_portfolio_weights.csv', index=False)

# Print the Optimal Weights for each stock

print(stock_list)
print(weights_array[index_max_sharpe,:])

#%%

'''VISUALIZE THE OPTIMAL PORTFOLIO AND PORTFOLIO SCENARIOS'''
# Identify the optimal portfolio in the returns and volatility arrays

max_sharpe_volatility = volatility_array[index_max_sharpe]
max_sharpe_return = returns_array[index_max_sharpe]

# Visualize volatility vs returns for each scenario

plt.figure(figsize=(12,8))

plt.scatter(volatility_array, returns_array, c=sharpe_array, cmap='viridis')

plt.colorbar(label='Sharpe Ratio')
plt.xlabel('volatility')
plt.ylabel('Return')

# Add the optimal portfolio to the visual

plt.scatter(max_sharpe_volatility,max_sharpe_return,c='orange',edgecolors='black')
plt.savefig('results/portfolio_optimization.png', dpi=300,bbox_inches='tight')

plt.show()





















