###############################################################################################################
# Developing a chatbot that will generate a weighted investment portfolio based on the user's risk tolerance  #                                                                                                            #
# and age, utilizing Streamlit, Python, Machine Learning, & Traditional Financial Metrics.                    #
###############################################################################################################

import streamlit as st
from streamlit_chat import message
from chatbot_functions import verifyUserAge

st.markdown("## Investment Portfolio Generator")

# Use the message function to create a chat-like UI
message("Hello, I'm a chatbot that can generate a weighted investment portfolio for you!", seed=21)
message("Please enter your age in the sidebar!", seed=21)

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
    
    else:
        # The user hasn't entered a response yet, so don't show any messages in the chat widget
        pass

except ValueError:
    message("I'm sorry, but it looks like you entered an invalid number for your age. Please enter a valid number!", seed=21)

# TO:DO --> grab user's investment amount, 
#           calculate weighted portfolio based off of 110 rule, 
#           display assets based off of user's chosen risk tolerance,
#           display dataframe of forecasts (Prophet Forecasts -- Short Term/Long Term ??) for chosen assets or display Monte Carlo Simulations
#           (in project requirments it says one or more machine learning models used, so we do not need to include LR Models or Decision Tree Models)