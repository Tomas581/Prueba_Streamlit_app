import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

from Functions import *
from Functions.URL_UTM_creator import URL_UTM_creator
from Functions.Check_spaces import check_spaces

# streamlit run URL_parameters_creator.py

# ------------------------------------------------------------------------------------------------------------------------------

st.title("URL with parameters creator")
st.subheader("Enter the following fields for the automatic URL.")
st.info("Fields marked down with an asterisk '*' must be filled the others are not required.")
st.divider()

# ------------------------------------------------------------------------------------------------------------------------------

st.text_input("Website URL *", key="URL")
st.text("The website URL must follow this format: https://www.example.com")
URL = check_spaces(st.session_state.URL)
if URL != "":   
    # Checks if the URL format is the correct one, if not displays an error message. 
    if URL[0:12] != "https://www.":
        st.error("The URL format is not correct :angry: :rage: :disappointed: :dizzy_face:") 
        
st.text_input("Campaign source *", key="utm_source")
utm_source = check_spaces(st.session_state.utm_source)
st.text("The campaign source: Instagram, Google...")

st.text_input("Campaign medium *", key="utm_medium")
utm_medium = check_spaces(st.session_state.utm_medium)
st.text("The campaign medium: Social, email, cpc... ")

st.text_input("Campaign name *", key="utm_campaign")
utm_campaign = check_spaces(st.session_state.utm_campaign)
st.text("The campaign name: Summer_big_sale")

st.text_input("Campaign id", key="utm_id")
utm_id = check_spaces(st.session_state.utm_id)
st.text("The ads campaign ID")

st.text_input("Campaign term", key="utm_term")
utm_term = check_spaces(st.session_state.utm_term)
st.text("The campaign keywords: beach_bag")

st.text_input("Campaign content", key="utm_content")
utm_content = check_spaces(st.session_state.utm_content)
st.text("To differentiate links")

# ------------------------------------------------------------------------------------------------------------------------------

st.divider()
st.subheader("Your URL with the entered parameters is the following:")
final_URL = URL_UTM_creator(URL, utm_source, utm_medium, utm_campaign, utm_id, utm_term, utm_content)

if final_URL != "":
    # Checks if the URL is not blank, if not displays copy button. 
    st.markdown("Click de following button to copy the link")
    st_copy_to_clipboard(final_URL)

