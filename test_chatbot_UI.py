###############################################################################################################
# Developing a chatbot that will generate a weighted investment portfolio based on the user's risk tolerance  #                                                                                                            #
# and age, utilizing Streamlit, Python, Machine Learning, & Traditional Financial Metrics.                    #
###############################################################################################################

import streamlit as st
from streamlit_chat import message

# Use the message function to create a chat-like UI
message("Hello, I'm a chatbot that can generate an investment portfolio for you!", seed=1)
message("Please enter your age in the sidebar!", seed=1)

# Ask the user for their age
user_age = st.sidebar.text_input("Enter your age: ")

# Check if the user has entered a response
if user_age:
    # Check if the user's age is a number
    if user_age.isdigit():
        # Convert the user's age to an integer
        age = int(user_age)

        # Check if the age is greater than or equal to 18
        if age >= 18:
            # Add a message to the chat widget indicating the user is over 18 years old
            message("You are over 18 years old! Enjoy the use of our investment portfolio generator!", seed=1)
        else:
            # Add a message to the chat widget indicating the user is under 18 years old
            message("This application requires you to be at least 18 years old.", seed=1)
    else:
        # Add a message to the chat widget indicating that the app isn't sure how to respond
        message("I'm sorry, I'm not sure how to respond to that.", seed=1)
else:
    # The user hasn't entered a response yet, so don't show any messages in the chat widget
    pass

# TO:DO --> grab user's investment amount, 
#           calculate weighted portfolio based off of 110 rule, 
#           display assets based off of user's chosen risk tolerance,
#           display dataframe of forecasts (Prophet Forecasts -- Short Term/Long Term ??) for chosen assets or display Monte Carlo Simulations
#           (in project requirments it says one or more machine learning models used, so we do not need to include LR Models or Decision Tree Models)