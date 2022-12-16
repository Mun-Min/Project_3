###############################################################################################################
#      This python file includes the neccesary functions that allow the chatbot's aggregations to run         #          
###############################################################################################################

from streamlit_chat import message
import streamlit as st

def verifyUserAge(age): 
    '''
    This function checks if the user's age is greater than or equal to 18
    
    Parameters: 

    age --> pass in the user's age from streamlit to verify if user is old enough to use the application
    '''
    # Check if the user's age is greater than or equal to 18
    if age >= 18:

        # Add a message to the chat widget indicating the user is over 18 years old
        message("You are over 18 years old! Enjoy the use of our investment portfolio generator!", seed=21)

    else:

        # Add a message to the chat widget indicating the user is under 18 years old or the input is not a valid age
        message("This application requires you to be at least 18 years old.", seed=21)

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
    portfolio_type --> pass in the chosen portfolio_type from streamlit to ensure weights are entered correctly
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
        user_buying_power_allocation.append('$' + str(investments_per_asset))
    
    message(f'Amount of buying power allocated towards each asset class (Stocks/Bonds/Crypto): ', seed=21, key=10)
    message(f'{user_buying_power_allocation}', seed=21, key=11)