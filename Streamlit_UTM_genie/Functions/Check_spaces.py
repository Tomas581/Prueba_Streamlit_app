import streamlit as st

# ------------------------------------------------------------------------------------------------------------------------------

def check_spaces(text):
    """
    This function checks if the text contains any spaces. 

    Parameters:
        The text to check. 
    Returns:
        In case there are no spaces, a success message is displayed.        
        In case there are any spaces, an error message is displayed, and the space is removed for later use.
    """
    if text == "":
        return ""
    new_text = ""
    cont = 0 
    for letter in text:
        if letter != " ":
            new_text = new_text + letter
        else: 
            cont = cont + 1
    if cont == 0:
        st.success("Your parameter is correct, it dos not contain any space :smiley: :smiley:")
    else: 
        st.error("Your parameter is incorrect, it contain at least one space :angry: :rage: :disappointed: :dizzy_face:")
    return new_text
