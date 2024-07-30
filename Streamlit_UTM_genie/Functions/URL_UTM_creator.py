import streamlit as st

# ------------------------------------------------------------------------------------------------------------------------------

def URL_UTM_creator(URL, utm_source, utm_medium, utm_campaign, utm_id = "", utm_term = "", utm_content = ""):
    """
    This function concatenates different strings with special characters. At first it checks if mandatory fields are not in blank.  

    Parameters:
        Text corresponding to its fields, the first four parameters must be fielded. For the function to work correctly, all fields should be without spaces.
    Return:
        The URL with all the parameters.
        In case any mandatory field is not filled, it displays an error.  
    """
    if URL == "" or utm_source == "" or utm_medium == "" or utm_campaign == "":
        st.error("There is a mandatory field empty. The URL can not be provided :angry: :rage: :disappointed: :dizzy_face:")
        return ""
    if URL[0:8] != "https://":
        st.error("The URL format is not correct :angry: :rage: :disappointed: :dizzy_face:") 
        return ""
    final_URL = URL + "?"  + "utm_source=" + utm_source + "&" + "utm_medium=" + utm_medium + "&" + "utm_campaign=" + utm_campaign
    if utm_id != "":
        final_URL = final_URL + "&" + "utm_id=" + utm_id
    if utm_term != "":
        final_URL = final_URL + "&" + "utm_term=" + utm_term
    if utm_content != "":
        final_URL = final_URL + "&" + "utm_content=" + utm_content
    container = st.container(border=True)
    container.markdown(final_URL)
    return final_URL
