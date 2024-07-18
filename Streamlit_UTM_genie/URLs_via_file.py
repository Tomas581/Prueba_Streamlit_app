import streamlit as st
import io
import csv

from Functions import *
from Functions.Remove_URL_spaces_csv import remove_URL_spaces_csv
from Functions.Remove_URL_spaces_xlsx import remove_URL_spaces_xlsx
# ------------------------------------------------------------------------------------------------------------------------------

st.title("UTM genie checker via file '.csv' or '.xlsx' :balloon:")
st.info("Upload a document in '.csv' or '.xlsx' format containing the URLs you want to verify. Make sure the first row of the document is a header, otherwise, the verification of the first URL will not be done.")
st.info("A new file is returned with the same extension, where the first column indicates the status of the original link, and the second column contains the corrected original URL if necessary.")
st.divider()

URL_file = st.file_uploader("Upload your file to check for possible spaces in the links. 📤", type=["xlsx", "csv"])
st.text_input("Enter the name you wish for your new document:", key="new_sheet")
new_file_name = str(st.session_state.new_sheet)

#------------------------------------------------------------------------------------------------------------------------------

if URL_file is not None:
    
    # First of all, checks if there is any attached file. If there is not any, does nothing.
    # Secondly, according to the file extension of the attached file, it executes the corresponding function to check the file.
    
    if URL_file.name.endswith('.xlsx'):
        remove_URL_spaces_xlsx(URL_file, st.session_state.new_sheet)

    elif URL_file.name.endswith('.csv'):
        URL_csv = io.StringIO(URL_file.getvalue().decode("utf-8"))
        URL_csv_lector = csv.reader(URL_csv)
        URLs = list(URL_csv_lector)
        remove_URL_spaces_csv(URLs, st.session_state.new_sheet)

