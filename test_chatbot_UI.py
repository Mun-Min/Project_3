###############################################################################################################
# Developing a chatbot that will generate a weighted investment portfolio based on the user's risk tolerance  # 
# and age, utilizing Streamlit, Python, Machine Learning, & Traditional Financial Metrics.                    #
###############################################################################################################

import streamlit as st
from streamlit_chat import message
from chatbot_functions import verifyUserAge
from chatbot_functions import determine_weights
from chatbot_functions import allocate_portfolio

st.markdown("## Investment Portfolio Generator")

# Use the message function to create a chat-like UI
message("Hello, I'm a chatbot that can generate a weighted investment portfolio for you!", seed=21)
message("Please enter your age", seed=21)

# Ask the user for their age
user_age = st.sidebar.text_input("Enter your age: ")
message(user_age, is_user=True, seed=1)

try: 

    # Check if the user has entered a response
    if user_age:

        # Convert the user's age to an integer
        age = float(user_age)

        # verify the user's age 
        verifyUserAge(age)

        if age >= 18: 

            # Ask the user for their desired investment amount 
            message("Please enter your desired investment amount in USD", seed=21, key=2)
            user_investment_amount = st.sidebar.text_input("Enter investment amount in USD: ", key=3)
            message(user_investment_amount, is_user=True, seed=1, key=4)
            
            # Ask the user for their desired portfolio type (risk tolerance)
            if user_investment_amount: 
                if user_investment_amount.isnumeric():
                    message("Please enter a portfolio type that matches your risk tolerance (High Risk Portfolio, Low Risk Portfolio, Moderate Risk Portfolio)", seed=21, key=5)
                    portfolio_type = st.sidebar.text_input('Choose one of the following: ')

                    valid_portfolio_types = ['high risk portfolio', 'low risk portfolio', 'moderate risk portfolio', 'high risk portfolio ', 'low risk portfolio ', 'moderate risk portfolio ']

                    if portfolio_type: 
                        if str(portfolio_type).lower() in valid_portfolio_types: 
                            if str(portfolio_type).lower() == 'high risk portfolio' or str(portfolio_type).lower() == 'high risk portfolio ': 

                                # generate a High Risk Portfolio based on expected return vs risk (MPT)
                                # stocks --> TSLA, NVDA 
                                # bonds --> Treasury Yield 10yr 
                                # crypto --> ETH

                                portfolio_list = ['TSLA', 'NVDA', '10yr Treasury Yield', 'ETH']
                                message('Your High-Risk Portfolio contains the following assets: ', seed=21, key=6)
                                message(f'{portfolio_list}', seed=21, key=7)

                                # calculate weights for portfolio
                                determine_weights(age)
                                allocate_portfolio(user_investment_amount)
                        else: 
                            message("I'm sorry, but it looks like you entered an invalid portfolio type. Please enter a valid portfolio type!", seed=21)
                else:
                    message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid number!", seed=21)
    else:
        # The user hasn't entered a response yet, so don't show any messages in the chat widget
        pass

except ValueError:
    message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid number!", seed=21)


# TO:DO --> grab user's investment amount, 
#           calculate weighted portfolio based off of 110 rule, 
#           display assets based off of user's chosen risk tolerance,
#           display dataframe of forecasts (Prophet Forecasts -- Short Term/Long Term ??) for chosen assets or display Monte Carlo Simulations
#           (in project requirments it says one or more machine learning models used, so we do not need to include LR Models or Decision Tree Models)