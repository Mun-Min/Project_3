###############################################################################################################
#      This python file includes the neccesary functions that allow the chatbot's aggregations to run         #          
###############################################################################################################

from streamlit_chat import message
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 
import time 

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

def display_forecasts(user_input, portfolio_type):
    '''
    This function will display the forecasts up to the next 30-days from our Prophet Models 
    
    Parameters: 

    user_input --> pass in the user_input from streamlit to verify if the user enters "yes" or "no" 
    '''

    if user_input:  
        if user_input.lower().strip() == 'yes' or user_input.lower().strip() == 'y': 
            
            message("Here you go!", seed=21, key=32)
            
            with st.spinner("Displaying Forecasts..."): 
                time.sleep(0.5)

                if str(portfolio_type).lower().strip() == 'high risk portfolio': 
                    #portfolio_list = ['TSLA', 'NVDA', '10-yr Treasury Yield', 'ETH']

                    # Create a list of dataframes and names for the charts
                    df_list = [
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/TSLA_forecast.csv'), 'TSLA'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/NVDA_forecast.csv'), 'NVDA'),
                                (pd.read_csv('./Data Collection Notebooks/bond_forecasts/10-yr Treasury Yield_forecast.csv'), '10-yr Treasury Yield'),
                                (pd.read_csv('./Data Collection Notebooks/crypto_forecasts/ETH-USD_forecast.csv'), 'ETH-USD')
                            ]
                 
                    # Use a dropdown menu to allow the user to select a chart
                    asset_selection = st.selectbox("Select Asset", options=[df[1] for df in df_list])
                    df, name = next((df for df in df_list if df[1] == asset_selection), None)
                    if df is not None:
                        df.rename(columns = {'ds':'Date'}, inplace = True)
                        df.reset_index(inplace = True)

                        # Load the historical prices for the selected asset
                        historical_prices_df = pd.read_csv(f'./Data Collection Notebooks/asset_historical_prices/{asset_selection}.csv')
                        historical_prices_df.rename(columns = {'Date':'Date'}, inplace = True)
                        historical_prices_df.reset_index(inplace = True)

                        # Create a line chart using plotly
                        trace_forecast = px.line(df, x='Date', y='Most Likely Case', title= f'{name} Forecasts up to the next 30 days')
                        trace_historical_prices = px.line(historical_prices_df, x='Date', y='Adj Close', title= f'{name} Historical Prices')
                        
                        # Display the charts one after the other
                        st.plotly_chart(trace_forecast, theme="streamlit", use_container_width=True)
                        st.plotly_chart(trace_historical_prices, theme="streamlit", use_container_width=True)
                        st.stop()

                if str(portfolio_type).lower().strip() == 'low risk portfolio': 
                    #portfolio_list = ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 
                    #                  'XOM', 'CVX','JPM', 'HD', 'V', '30-yr Treasury Yield', 'BTC']
                    
                    # Create a list of dataframes and names for the charts
                    df_list = [
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PEP_forecast.csv'), 'PEP'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PG_forecast.csv'), 'PG'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/KO_forecast.csv'), 'KO'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/JNJ_forecast.csv'), 'JNJ'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/BRK-B_forecast.csv'), 'BRK-B'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MRK_forecast.csv'), 'MRK'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PFE_forecast.csv'), 'PFE'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/XOM_forecast.csv'), 'XOM'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/CVX_forecast.csv'), 'CVX'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/JPM_forecast.csv'), 'JPM'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/HD_forecast.csv'), 'HD'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/V_forecast.csv'), 'V'),
                                (pd.read_csv('./Data Collection Notebooks/bond_forecasts/30-yr Treasury Yield_forecast.csv'), '30-yr Treasury Yield'),
                                (pd.read_csv('./Data Collection Notebooks/crypto_forecasts/BTC-USD_forecast.csv'), 'BTC-USD')
                            ]

                    # Use a dropdown menu to allow the user to select a chart
                    asset_selection = st.selectbox("Select Asset", options=[df[1] for df in df_list])
                    df, name = next((df for df in df_list if df[1] == asset_selection), None)
                    if df is not None:
                        df.rename(columns = {'ds':'Date'}, inplace = True)
                        df.reset_index(inplace = True)

                        # Load the historical prices for the selected asset
                        historical_prices_df = pd.read_csv(f'./Data Collection Notebooks/asset_historical_prices/{asset_selection}.csv')
                        historical_prices_df.rename(columns = {'Date':'Date'}, inplace = True)
                        historical_prices_df.reset_index(inplace = True)

                        # Create a line chart using plotly
                        trace_forecast = px.line(df, x='Date', y='Most Likely Case', title= f'{name} Forecasts up to the next 30 days')
                        trace_historical_prices = px.line(historical_prices_df, x='Date', y='Adj Close', title= f'{name} Historical Prices')
                        
                        # Display the charts one after the other
                        st.plotly_chart(trace_forecast, theme="streamlit", use_container_width=True)
                        st.plotly_chart(trace_historical_prices, theme="streamlit", use_container_width=True)
                        st.stop()

                if str(portfolio_type).lower().strip() == 'moderate risk portfolio':
                    #portfolio_list = ['UNH', 'MSFT', 'LLY', 'MA', 'GOOG', 'GOOGL', 'ABBV', 
                    #                  'BAC', 'AAPL','AMZN', 'META', '30yr Treasury Yield', 'BTC']

                    # Create a list of dataframes and names for the charts
                    df_list = [
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/UNH_forecast.csv'), 'UNH'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MSFT_forecast.csv'), 'MSFT'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/LLY_forecast.csv'), 'LLY'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MA_forecast.csv'), 'MA'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/GOOG_forecast.csv'), 'GOOG'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/GOOGL_forecast.csv'), 'GOOGL'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/ABBV_forecast.csv'), 'ABBV'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/BAC_forecast.csv'), 'BAC'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/AAPL_forecast.csv'), 'AAPL'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/AMZN_forecast.csv'), 'AMZN'),
                                (pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/META_forecast.csv'), 'META'),
                                (pd.read_csv('./Data Collection Notebooks/bond_forecasts/30-yr Treasury Yield_forecast.csv'), '30-yr Treasury Yield'),
                                (pd.read_csv('./Data Collection Notebooks/crypto_forecasts/BTC-USD_forecast.csv'), 'BTC-USD')
                            ]

                    # Use a dropdown menu to allow the user to select a chart
                    asset_selection = st.selectbox("Select Asset", options=[df[1] for df in df_list])
                    df, name = next((df for df in df_list if df[1] == asset_selection), None)
                    if df is not None:
                        df.rename(columns = {'ds':'Date'}, inplace = True)
                        df.reset_index(inplace = True)

                        # Load the historical prices for the selected asset
                        historical_prices_df = pd.read_csv(f'./Data Collection Notebooks/asset_historical_prices/{asset_selection}.csv')
                        historical_prices_df.rename(columns = {'Date':'Date'}, inplace = True)
                        historical_prices_df.reset_index(inplace = True)

                        # Create a line chart using plotly
                        trace_forecast = px.line(df, x='Date', y='Most Likely Case', title= f'{name} Forecasts up to the next 30 days')
                        trace_historical_prices = px.line(historical_prices_df, x='Date', y='Adj Close', title= f'{name} Historical Prices')
                        
                        # Display the charts one after the other
                        st.plotly_chart(trace_forecast, theme="streamlit", use_container_width=True)
                        st.plotly_chart(trace_historical_prices, theme="streamlit", use_container_width=True)
                        st.stop()

        if user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
            message("Thank you for using our investment portfolio generator!", seed=21, key=33)
            st.balloons() 
    
        else: 
            message("Please enter either 'yes' or 'no'", seed=21, key=34)
