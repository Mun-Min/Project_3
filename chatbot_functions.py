###############################################################################################################
#      This python file includes the neccesary functions that allow the chatbot's aggregations to run         #          
###############################################################################################################

from streamlit_chat import message
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd 

def verifyUserAge(age): 
    '''
    This function checks if the user's age is greater than or equal to 18
    
    Parameters: 

    age --> pass in the user's age from streamlit to verify if user is old enough to use the application
    '''
    # Check if the user's age is greater than or equal to 18
    if age >= 18 and age <= 110:

        # Add a message to the chat widget indicating the user is over 18 years old
        message("You are over 18 years old! Enjoy the use of our investment portfolio generator!", seed=21, key=23)
    
    elif age > 110: 
        message("I'm sorry, but it looks like you are too old to use this application. Please enter an age less than 110!", seed=21, key=24)
    
    else:
        # Add a message to the chat widget indicating the user is under 18 years old or the input is not a valid age
        message("This application requires you to be at least 18 years old!", seed=21, key=25)

portfolio_list = []
weights_list = []
user_buying_power_allocation = []

#@st.cache(max_entries=1, allow_output_mutation=True) 
def determine_weights(age): 
    '''
    This function calculates the weights for the chosen portfolio based off of the 
    user's age and a traditional investment strategy called the 110 rule 
    
    Parameters: 

    age --> pass in the user's age from streamlit to be calculated through the 110 rule
    '''
    weights_list.clear()

    user_stock_weights = 110 - age
    user_bonds_crypto_weights = (100 - user_stock_weights) / 2

    user_bonds_crypto_weights = user_bonds_crypto_weights / 100
    user_stock_weights = user_stock_weights / 100
    
    weights_list.append(user_stock_weights)
    weights_list.append(user_bonds_crypto_weights)
    weights_list.append(user_bonds_crypto_weights)
    
def allocate_portfolio(user_investment_amount): 
    '''
    This function allocates the user's buying power towards each asset class based on the weights calculated above
    
    Parameters: 

    user_investment_amount --> pass in the user_investment_amount from streamlit to calculate how much money the user will invest in each asset class
    '''
    user_buying_power_allocation.clear()

    for weight in weights_list: 
        investments_per_asset = float(user_investment_amount) * float(weight)
        investments_per_asset = round(investments_per_asset, 2)
        investments_per_asset = '${:,.2f}'.format(investments_per_asset)
        user_buying_power_allocation.append(str(investments_per_asset))
    
    assets = ['Stocks', 'Bonds', 'Crypto']
    values = user_buying_power_allocation
    #df = pd.DataFrame({'Asset': assets, 'Value': values})
    message(f'I recommend allocating your buying power towards each asset class in the following format: ', seed=21, key=26)
    
    st.table(pd.DataFrame({'Asset': assets, 'Value': values}))
    
    #message(f'(Stocks/Bonds/Crypto) -- {user_buying_power_allocation}', seed=21, key=11)

def display_portfolio_allocation(portfolio_type): 
    '''
    This function displays the user's portfolio allocation via a plotly pie chart 
    
    Parameters: 

    portfolio_type --> pass in the portfolio_type from streamlit to check which portfolio the user chose
    '''

    if str(portfolio_type).lower().strip() == 'low risk portfolio':
        
        # Set the labels for the pie chart
        # portfolio_list = ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 
        #               'XOM', 'CVX','JPM', 'HD', 'V', '30yr Treasury Yield', 'BTC']

        # Set the labels for the pie chart
        labels = ["Stocks", "Bonds", "Crypto"]

        # Set the sizes for each pie slice based on the weights calculated in the determine_weights function
        sizes = weights_list 

        # Set the colors for each pie slice
        #colors = ['#ff9999','#66b3ff','#99ff99']

        # Set the stock lists for each asset type
        stocks = ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 'XOM', 'CVX','JPM', 'HD', 'V']
        bonds = ['30yr Treasury Yield']
        crypto = ['BTC']

        # Create a list of lists containing the stock lists for each asset type
        #hover_data = [[', '.join(stocks)], [', '.join(bonds)], [', '.join(crypto)]]

        # Create the pie chart using the go.Pie object
        fig = px.pie(values=sizes, names=labels, title='Asset Allocation', hole=.3)

        # Display the pie chart using st.plotly_chart
        st.plotly_chart(fig)    

    if str(portfolio_type).lower().strip() == 'moderate risk portfolio':
        
        # Set the labels for the pie chart
        # labels = ['UNH', 'MSFT', 'LLY', 'MA', 'GOOG', 'GOOGL', 'ABBV', 
        #           'BAC', 'AAPL','AMZN', 'META', '30yr Treasury Yield', 'BTC']

        labels = ["Stocks", "Bonds", "Crypto"]

        # Set the sizes for each pie slice based on the weights calculated in the determine_weights function
        sizes = weights_list 

        # Set the colors for each pie slice
        #colors = ['#ff9999','#66b3ff','#99ff99']

        # Create the pie chart using the go.Pie object
        fig = px.pie(values=sizes, names=labels, title='Asset Allocation', hole=.3)

        # Display the pie chart using st.plotly_chart
        st.plotly_chart(fig)

    if str(portfolio_type).lower().strip() == 'high risk portfolio':
        
        # Set the labels for the pie chart
        #labels = ['TSLA', 'NVDA', '10yr Treasury Yield', 'ETH']

        labels = ["Stocks", "Bonds", "Crypto"]

        # Set the sizes for each pie slice based on the weights calculated in the determine_weights function
        sizes = weights_list 

        # Set the colors for each pie slice
        #colors = ['#ff9999','#66b3ff','#99ff99']

        # Create the pie chart using the go.Pie object
        fig = px.pie(values=sizes, names=labels, title='Asset Allocation', hole=.3)

        # Display the pie chart using st.plotly_chart
        st.plotly_chart(fig)

def display_forecasts(user_input):
    '''
    This function will display the forecasts up to the next 30-days from our Prophet Models 
    
    Parameters: 

    user_input --> pass in the user_input from streamlit to verify if the user enters "yes" or "no" 
    '''

    if user_input:  
        if user_input.lower().strip() == 'yes' or user_input.lower().strip() == 'y': 
            message("TO:DO -- DISPLAY FORECASTS FROM PROPHET MODELS", seed=21, key=32)
    
        elif user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
            message("Thank you for using our investment portfolio generator!", seed=21, key=33)
    
        else: 
            message("Please enter either 'yes' or 'no'", seed=21, key=34)
