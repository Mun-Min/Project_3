from streamlit_chat import message

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
