import streamlit as st

# ------------------------------------------------------------------------------------------------------------------------------

def remove_URL_spaces(url):
    """
    This function allows to remove all possible spaces presents in URLs, it's worth noting that the space must be represented with the following symbol: %.
    
    Parameters: 
        The input parameter has to be the URL that you want to check.
    Returns: 
        In case the URL contains any spaces, return the same URL with all spaces removed, and indicate the number of spaces that were present.
        If the URL does not contain any spaces, return a message indicating accordingly. 
    """
    new_URL = ""
    num_spaces = 0
    if "%" in url: 
        for letter in url:
            if letter != "%":
                new_URL = new_URL + letter
            elif letter == "%":
                num_spaces = num_spaces + 1
        st.warning("There were " + str(num_spaces) + " spaces in your URL, this is your new URL without spaces: ") 
        container = st.container(border=True)
        container.markdown(new_URL)
        return new_URL
    elif url == "":
        return("")
    else:
        st.balloons()
        return(st.success("There are no spaces in your URL :smiley: :smiley:"))
