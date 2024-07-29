# Streamlit_UTM_genie
## Description
##### Streamlit UTM Genie is a Streamlit-based website that incorporates the functionalities of the UTM_genie library to enhance user experience.
##### It features four distinct pages, each offering different functionalities: "Fast URL checker", "URLs via file", "URL parameters creator", "UTM Campaign Builder".
***

### Fast URL checker
##### This page allows you to quickly check if a URL contains spaces and, if so, remove them and return the corrected URL.
#### How does it work?
##### When a URL is entered, the function "remove_URL_spaces('URL')" is executed, where the input parameter is the entered URL. This function checks whether the link contains spaces. If spaces are found, it indicates the number of spaces present and returns the original URL with the spaces removed. Otherwise, it displays a message indicating that there are no spaces in the URL.
***

### URLs via file
##### This page allows an effective verification of a large number of URLs to determine if they contain spaces or not. Uploaded files must have the extensions '.csv' or '.xlsx'.
### How does it work?
##### Once the document to be checked is uploaded and the optional field below is filled out, the function "identify_file_type('File Name to Verify', 'New File Name')" is executed. This function identifies the file's extension to execute the corresponding operation. The first input is the file name with its corresponding extension, either '.csv' or '.xlsx', and the second input is the string for the desired name of the new file. If the second input is not provided, a default name is set.
### CSV File
##### If it is a '.csv' file, it executes the function "remove_URL_spaces_csv("File Name to Verify", "New File Name")" for verification. The first input parameter is a string representing the name of the file to be checked, assuming by default that the file has a header which is not analyzed. The second parameter can be the name of the new file where corrections are desired. This function checks all URLs present in the first column; the first row is not checked. If any spaces are found, they are removed. Once the process is completed, the new file can be downloaded, where the first column refers to the status of the original URL, and the second column contains the original URL with any necessary corrections.
### Excel File '.xlsx'
##### If it is a '.xlsx' file, the function remove_URL_spaces_xlsx("File name to verify", "New sheet name") is executed for verification. The first input parameter is the string containing the file name. By default, it assumes the file has a header that will not be analyzed. The second parameter can be the name of the new sheet to be created for storing corrections. This function checks all URLs present in the first column; the first row is not checked. Any spaces found within URLs are removed during this process. Once the process is complete, the modified file can be downloaded. The resulting file contains two sheets: the first identical to the original uploaded by the user, and the second where the first column indicates the status of the original URL and the second column contains the original URL with corrections applied, if necessary.
***

### URL parameters creator
##### This page allows creating a URL with fully customizable UTM parameters, ensuring that the final URL does not contain any spaces.
### How does it work?
##### The user must fill in the fields with essential information as deemed necessary; the first four fields are mandatory. Firstly, it verifies that the initial fields are not empty and ensures that the "URL" field is in the correct format. Subsequently, the function "check_spaces('UTM Parameter')" checks whether the parameters contains any spaces. If so, it returns an error message and corrects the parameter to prevent errors in the final URL; otherwise, it confirms the absence of spaces. Once all parameters are validated, the function "URL_UTM_creator('URL', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_id', 'utm_term', 'utm_content')" is executed to properly format the final URL, and a button is displayed to copy it.
