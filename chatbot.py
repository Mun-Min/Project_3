###############################################################################################################
# Developing a chatbot that will generate a weighted investment portfolio based on the user's risk tolerance  # 
# and age, utilizing Streamlit, Python, Machine Learning, & Traditional Financial Metrics.                    #
###############################################################################################################

# import libraries 
import streamlit as st
from streamlit_chat import message
import pandas as pd

from chatbot_functions import verifyUserAge
from chatbot_functions import determine_weights
from chatbot_functions import allocate_portfolio
from chatbot_functions import display_portfolio_allocation
from chatbot_functions import display_forecasts


st.markdown("## Investment Portfolio Generator")
st.markdown("---")

# chatbot function
def chatbot():
    # Use the message function to create a chat-like UI
    message("Hello, I'm a chatbot that can generate a weighted investment portfolio for you!", seed=21, key=10)
    message("Please enter your age", seed=21, key=11)

    # Ask the user for their age
    user_age = st.sidebar.text_input("Enter your age: ")
    message(user_age, is_user=True, seed=1, key=12)


    # Check if the user has entered a response
    if user_age:
    
        if user_age.isdigit() == False: 
            message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid number!", seed=21, key=13)
    
        else:
            # Convert the user's age to an integer
            age = float(user_age)
            
            # verify the user's age 
            verifyUserAge(age)

            if age >= 18 and age <= 110: 

                # Ask the user for their desired investment amount 
                message("Please enter your desired investment amount in USD", seed=21, key=14)
                user_investment_amount = st.sidebar.text_input("Enter investment amount in USD: ")
                message(user_investment_amount, is_user=True, seed=1, key=15)
            
                # Ask the user for their desired portfolio type (risk tolerance)
                if user_investment_amount: 
                    if user_investment_amount.isnumeric():
                        message("Please enter a portfolio type that matches your risk tolerance (High Risk Portfolio, Low Risk Portfolio, Moderate Risk Portfolio)", seed=21, key=16)
                        portfolio_type = st.sidebar.text_input('Enter portfolio type: ')

                        valid_portfolio_types = ['high risk portfolio', 'low risk portfolio', 'moderate risk portfolio']

                        if portfolio_type: 
                            if str(portfolio_type).lower().strip() in valid_portfolio_types: 
                                if str(portfolio_type).lower().strip() == 'high risk portfolio': 

                                    # generate a High Risk Portfolio based on expected return vs risk (MPT)
                                    # stocks --> TSLA, NVDA 
                                    # bonds --> Treasury Yield 10yr 
                                    # crypto --> ETH

                                    #portfolio_list = ['TSLA', 'NVDA', '10yr Treasury Yield', 'ETH']
                                    #df = pd.DataFrame({'Chosen Assets': portfolio_list})

                                    df = pd.DataFrame({'Stocks': ['TSLA', 'NVDA'], 'Bonds': ['10yr Treasury Yield', '-'], 'Crypto': ['ETH', '-']})
                                    message('Your High-Risk Portfolio contains the following assets: ', seed=21, key=17)
                                    st.table(df) 

                                    #message(f'{portfolio_table}', seed=21, key=7)

                                    # calculate weights for portfolio
                                    determine_weights(age)
                                    allocate_portfolio(user_investment_amount)
                                    
                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=30)
                                    user_input = st.sidebar.text_input("Display forecasts? (yes/no): ")
                                    message(user_input, is_user=True, seed=1, key=31)

                                    # display prophet model forecasts
                                    display_forecasts(user_input)
                                
                                if str(portfolio_type).lower().strip() == 'low risk portfolio': 

                                    # generate a Low Risk Portfolio based on expected return vs risk 
                                    # stocks --> PEP, PG, KO, JNJ, BRK-B, MRK, PFE, XOM, CVX, JPM, HD, V 
                                    # bonds --> Treasury Yield 30yr 
                                    # crypto --> BTC

                                    #portfolio_list = ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 
                                    #                  'XOM', 'CVX','JPM', 'HD', 'V', '30yr Treasury Yield', 'BTC']
                                    #df = pd.DataFrame({'Chosen Assets': portfolio_list})

                                    df = pd.DataFrame(
                                        {'Stocks': ['PEP', 'PG', 'KO', 'JNJ', 'BRK-B', 'MRK', 'PFE', 'XOM', 'CVX','JPM', 'HD', 'V'], 
                                         'Bonds': ['30yr Treasury Yield', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
                                         'Crypto': ['BTC', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
                                        })
                                    message('Your Low-Risk Portfolio contains the following assets: ', seed=21, key=18)
                                    st.table(df) 
                                
                                    #message(f'{portfolio_list}', seed=21, key=13)
                                

                                    # calculate weights for portfolio
                                    determine_weights(age)                               
                                    allocate_portfolio(user_investment_amount)
    
                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=35)
                                    user_input = st.sidebar.text_input("Display forecasts? (yes/no): ")
                                    message(user_input, is_user=True, seed=1, key=36)

                                    # display prophet model forecasts
                                    display_forecasts(user_input)

                                if str(portfolio_type).lower().strip() == 'moderate risk portfolio': 

                                    # generate a Moderate Risk Portfolio portfolio based on expected return vs risk 
                                    # stocks --> UNH, MSFT, LLY, MA, GOOG, GOOGL, ABBV, BAC, AAPL, AMZN, META
                                    # bonds --> Treasury Yield 30yr 
                                    # crypto --> BTC

                                    #portfolio_list = ['UNH', 'MSFT', 'LLY', 'MA', 'GOOG', 'GOOGL', 'ABBV', 
                                    #                  'BAC', 'AAPL','AMZN', 'META', '30yr Treasury Yield', 'BTC']
                                    #df = pd.DataFrame({'Chosen Assets': portfolio_list})

                                    df = pd.DataFrame(
                                        {'Stocks': ['UNH', 'MSFT', 'LLY', 'MA', 'GOOG', 'GOOGL', 'ABBV', 'BAC', 'AAPL','AMZN', 'META'], 
                                         'Bonds': ['30yr Treasury Yield', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
                                         'Crypto': ['BTC', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
                                        })
                                    message('Your Moderate-Risk Portfolio contains the following assets: ', seed=21, key=19)
                                    st.table(df) 

                                    #message(f'{portfolio_list}', seed=21, key=15)

                                    # calculate weights for portfolio
                                    determine_weights(age)
                                    allocate_portfolio(user_investment_amount)

                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=37)
                                    user_input = st.sidebar.text_input("Display forecasts? (yes/no): ")
                                    message(user_input, is_user=True, seed=1, key=38)

                                    # display prophet model forecasts
                                    display_forecasts(user_input)

                            else: 
                                message("I'm sorry, but it looks like you entered an invalid portfolio type. Please enter a valid portfolio type!", seed=21, key=20)
                    else:
                        message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid number!", seed=21)
    else:
        # The user hasn't entered a response yet, so don't show any messages in the chat widget
        pass

# call chatbot function 
chatbot() 


# TO:DO --> display forecasts for selected stocks/bonds/crypto 
#           display monte carlo simulations for each portfolio type 