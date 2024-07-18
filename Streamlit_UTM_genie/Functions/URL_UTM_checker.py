import streamlit as st
from Functions import *
from Functions.Remove_URL_spaces import remove_URL_spaces

# ------------------------------------------------------------------------------------------------------------------------------

def URL_UTM_checker(URL):
    """"
    This function allows you to do a quick check for existing spaces in the entered URL.  It is important to note that the space must be represented by the following symbol: %. 
    
    Parameters: 
        The input parameter has to be the URL that you want to check.
    Returns: 
        In case the URL has any spaces, this calls the function 'sacar_espacio_URL' and removes them.
        In case the URL does not contain any spaces, it returns a message indicating the corresponding information and balloons are displayed.
    """
    if "%" in URL:
        remove_URL_spaces(URL)
    elif URL == "":
        return("")
    else:
        st.balloons()
        return(st.success("There are no spaces in your URL :smiley: :smiley:"))     
