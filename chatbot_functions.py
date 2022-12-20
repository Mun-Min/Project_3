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
            message("TO:DO -- DISPLAY FORECASTS FROM PROPHET MODELS", seed=21, key=32)

            if str(portfolio_type).lower().strip() == 'high risk portfolio': 
                #portfolio_list = ['TSLA', 'NVDA', '10yr Treasury Yield', 'ETH']

                st.markdown('#### TSLA Forecasts up to the next 30 days')
                tsla_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/TSLA_forecast.csv')
                tsla_df.rename(columns = {'ds':'Date'}, inplace = True)

                
                # Create a trace for the TSLA data
                tsla_df.reset_index(inplace = True)
                tsla_trace = px.line(tsla_df, x='Date', y='Most Likely Case')
                st.plotly_chart(tsla_trace, theme="streamlit", use_container_width=True)


                st.markdown('#### NVDA Forecasts up to the next 30 days')
                nvda_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/NVDA_forecast.csv')
                nvda_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the NVDA data
                nvda_df.reset_index(inplace = True)
                nvda_trace = px.line(nvda_df, x='Date', y='Most Likely Case')
                st.plotly_chart(nvda_trace, theme="streamlit", use_container_width=True)
            
            if str(portfolio_type).lower().strip() == 'low risk portfolio': 
                #portfolio_list = ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 
                #                  'XOM', 'CVX','JPM', 'HD', 'V', '30yr Treasury Yield', 'BTC']

                st.markdown('#### PEP Forecasts up to the next 30 days')
                pep_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PEP_forecast.csv')
                pep_df.rename(columns = {'ds':'Date'}, inplace = True)
              
                # Create a trace for the PEP data
                pep_df.reset_index(inplace = True)
                pep_trace = px.line(pep_df, x='Date', y='Most Likely Case')
                st.plotly_chart(pep_trace, theme="streamlit", use_container_width=True)


                st.markdown('#### PG Forecasts up to the next 30 days')
                pg_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PG_forecast.csv')
                pg_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the PG data
                pg_df.reset_index(inplace = True)
                pg_trace = px.line(pg_df, x='Date', y='Most Likely Case')
                st.plotly_chart(pg_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### KO Forecasts up to the next 30 days')
                ko_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/KO_forecast.csv')
                ko_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the KO data
                ko_df.reset_index(inplace = True)
                ko_trace = px.line(ko_df, x='Date', y='Most Likely Case')
                st.plotly_chart(ko_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### JNJ Forecasts up to the next 30 days')
                jnj_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/JNJ_forecast.csv')
                jnj_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the JNJ data
                jnj_df.reset_index(inplace = True)
                jnj_trace = px.line(jnj_df, x='Date', y='Most Likely Case')
                st.plotly_chart(jnj_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### BRK-B Forecasts up to the next 30 days')
                brkb_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/BRK-B_forecast.csv')
                brkb_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the BRK-B data
                brkb_df.reset_index(inplace = True)
                brkb_trace = px.line(brkb_df, x='Date', y='Most Likely Case')
                st.plotly_chart(brkb_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### MRK Forecasts up to the next 30 days')
                mrk_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MRK_forecast.csv')
                mrk_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the MRK data
                mrk_df.reset_index(inplace = True)
                mrk_trace = px.line(mrk_df, x='Date', y='Most Likely Case')
                st.plotly_chart(mrk_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### PFE Forecasts up to the next 30 days')
                pfe_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/PFE_forecast.csv')
                pfe_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the PFE data
                pfe_df.reset_index(inplace = True)
                pfe_trace = px.line(pfe_df, x='Date', y='Most Likely Case')
                st.plotly_chart(pfe_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### XOM Forecasts up to the next 30 days')
                xom_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/XOM_forecast.csv')
                xom_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the XOM data
                xom_df.reset_index(inplace = True)
                xom_trace = px.line(xom_df, x='Date', y='Most Likely Case')
                st.plotly_chart(xom_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### CVX Forecasts up to the next 30 days')
                cvx_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/CVX_forecast.csv')
                cvx_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the CVX data
                cvx_df.reset_index(inplace = True)
                cvx_trace = px.line(cvx_df, x='Date', y='Most Likely Case')
                st.plotly_chart(cvx_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### JPM Forecasts up to the next 30 days')
                jpm_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/JPM_forecast.csv')
                jpm_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the JPM data
                jpm_df.reset_index(inplace = True)
                jpm_trace = px.line(jpm_df, x='Date', y='Most Likely Case')
                st.plotly_chart(jpm_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### HD Forecasts up to the next 30 days')
                hd_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/HD_forecast.csv')
                hd_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the HD data
                hd_df.reset_index(inplace = True)
                hd_trace = px.line(hd_df, x='Date', y='Most Likely Case')
                st.plotly_chart(hd_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### V Forecasts up to the next 30 days')
                v_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/V_forecast.csv')
                v_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the V data
                v_df.reset_index(inplace = True)
                v_trace = px.line(v_df, x='Date', y='Most Likely Case')
                st.plotly_chart(v_trace, theme="streamlit", use_container_width=True)

            if str(portfolio_type).lower().strip() == 'moderate risk portfolio':
                #portfolio_list = ['UNH', 'MSFT', 'LLY', 'MA', 'GOOG', 'GOOGL', 'ABBV', 
                #                  'BAC', 'AAPL','AMZN', 'META', '30yr Treasury Yield', 'BTC']

                st.markdown('#### UNH Forecasts up to the next 30 days')
                unh_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/UNH_forecast.csv')
                unh_df.rename(columns = {'ds':'Date'}, inplace = True)
              
                # Create a trace for the UNH data
                unh_df.reset_index(inplace = True)
                unh_trace = px.line(unh_df, x='Date', y='Most Likely Case')
                st.plotly_chart(unh_trace, theme="streamlit", use_container_width=True)


                st.markdown('#### MSFT Forecasts up to the next 30 days')
                msft_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MSFT_forecast.csv')
                msft_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the MSFT data
                msft_df.reset_index(inplace = True)
                msft_trace = px.line(msft_df, x='Date', y='Most Likely Case')
                st.plotly_chart(msft_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### LLY Forecasts up to the next 30 days')
                lly_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/LLY_forecast.csv')
                lly_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the LLY data
                lly_df.reset_index(inplace = True)
                lly_trace = px.line(lly_df, x='Date', y='Most Likely Case')
                st.plotly_chart(lly_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### MA Forecasts up to the next 30 days')
                ma_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/MA_forecast.csv')
                ma_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the MA data
                ma_df.reset_index(inplace = True)
                ma_trace = px.line(ma_df, x='Date', y='Most Likely Case')
                st.plotly_chart(ma_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### GOOG Forecasts up to the next 30 days')
                goog_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/GOOG_forecast.csv')
                goog_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the GOOG data
                goog_df.reset_index(inplace = True)
                goog_trace = px.line(goog_df, x='Date', y='Most Likely Case')
                st.plotly_chart(goog_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### GOOGL Forecasts up to the next 30 days')
                googl_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/GOOGL_forecast.csv')
                googl_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the GOOGL data
                googl_df.reset_index(inplace = True)
                googl_trace = px.line(googl_df, x='Date', y='Most Likely Case')
                st.plotly_chart(googl_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### ABBV Forecasts up to the next 30 days')
                abbv_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/ABBV_forecast.csv')
                abbv_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the ABBV data
                abbv_df.reset_index(inplace = True)
                abbv_trace = px.line(abbv_df, x='Date', y='Most Likely Case')
                st.plotly_chart(abbv_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### BAC Forecasts up to the next 30 days')
                bac_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/BAC_forecast.csv')
                bac_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the BAC data
                bac_df.reset_index(inplace = True)
                bac_trace = px.line(bac_df, x='Date', y='Most Likely Case')
                st.plotly_chart(bac_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### AAPL Forecasts up to the next 30 days')
                aapl_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/AAPL_forecast.csv')
                aapl_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the AAPL data
                aapl_df.reset_index(inplace = True)
                aapl_trace = px.line(aapl_df, x='Date', y='Most Likely Case')
                st.plotly_chart(aapl_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### AMZN Forecasts up to the next 30 days')
                amzn_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/AMZN_forecast.csv')
                amzn_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the AMZN data
                amzn_df.reset_index(inplace = True)
                amzn_trace = px.line(amzn_df, x='Date', y='Most Likely Case')
                st.plotly_chart(amzn_trace, theme="streamlit", use_container_width=True)

                st.markdown('#### META Forecasts up to the next 30 days')
                meta_df = pd.read_csv('./Data Collection Notebooks/top25_SP500_forecasts/META_forecast.csv')
                meta_df.rename(columns = {'ds':'Date'}, inplace = True)

                # Create a trace for the META data
                meta_df.reset_index(inplace = True)
                meta_trace = px.line(meta_df, x='Date', y='Most Likely Case')
                st.plotly_chart(meta_trace, theme="streamlit", use_container_width=True)

        elif user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
            message("Thank you for using our investment portfolio generator!", seed=21, key=33)
    
        else: 
            message("Please enter either 'yes' or 'no'", seed=21, key=34)
