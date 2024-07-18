import streamlit as st

from Functions import *
from Functions.Remove_URL_spaces import remove_URL_spaces

# ------------------------------------------------------------------------------------------------------------------------------

st.title("UTM genie :balloon:")
st.text("")
st.subheader("Enter the URL of the link you want to verify.")
st.info("In case the URL does not contain any spaces, the appropriate message will be given.")
st.info("In case the URL contains spaces, this circumstance will be indicated along with the number of spaces present, and the original URL with the spaces removed will also be provided.")
st.divider()
st.text_input("Enter your URL to check for spaces and, if found, remove them:", key="url_to_check")
st.text("")
st.markdown(st.session_state.url_to_check)

# ------------------------------------------------------------------------------------------------------------------------------

remove_URL_spaces(st.session_state.url_to_check)

