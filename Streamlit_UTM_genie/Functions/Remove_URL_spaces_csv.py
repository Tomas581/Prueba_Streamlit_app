import streamlit as st
import io
import csv

# ------------------------------------------------------------------------------------------------------------------------------

def remove_URL_spaces_csv(doc, new_doc="New URL file"):
    """
    This function allows to remove all possible spaces presents in URLs, it's worth noting that the space must be represented with the following symbol: %.

    Parameters:
        First, a document of type '.csv' containing the links to be verified.
        The second can be a previously created '.csv' document or the name of the document you wish to be created for making the corrections, ending with the extension '.csv'.
    The function edits or creates the second document where in the first column displays a message with the status of the original URL, and the next one shows either the original URL or the new one depending on the status of the original URL.
        If the original URL contains any spaces, a message indicating this issue is returned, along with the number of spaces it contained and the same URL with all spaces removed and ready to be used!
        If the URL does not contain any spaces, a message indicating this is returned along with the original URL.
    Returns:
        The corresponding document. 
    """
    output = io.StringIO()  # Create a StringIO object to store the CSV in memory.
    new_URL_file = csv.writer(output)  # Create a CSV writer that will write to the StringIO object.
    for url_index, url in enumerate(doc[1:]): # Iterate over all the URLs in the document.
        for i in url: # i is the iterated URL.
            if "%" in i: 
                new_URL = ""
                num_espaces = 0
                for letter in i:
                    if letter != "%":
                        new_URL = new_URL + letter
                    elif letter == "%":
                         num_espaces = num_espaces + 1
                message = ("There were " + str(num_espaces) + " spaces in your URL on line " + str(url_index+1) + " this is your new URL without spaces" + "; " + new_URL)
                new_URL_file.writerow([message])
            else:
                message = ("There were no space in your URL on the line " + str(url_index+1) + "; " + i)
                new_URL_file.writerow([message])
    final_new_URL_file = output.getvalue()  # Get the content of the StringIO object as a string.
    st.download_button(label = " 📥 Download file with corrected URLs", data = final_new_URL_file, file_name= new_doc +".csv", mime='text/csv')
