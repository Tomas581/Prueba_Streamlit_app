from setuptools import setup, find_packages

setup(
    name='Streamlit_UTM_genie',
    version='0.1.0', 
    description='A Streamlit application designed for the verification and modification of URLs. Users can upload individual URLs or submit files in ".csv" or ".xlsx" formats containing URLs for analysis. The program detects and removes any space within the URLs to ensure their correctness. Additionally, the application provides functionality for generating URLs with campaign UTM parameters by filling in various fields. All input fields are validated to prevent unwanted spaces, ensuring the creation of accurate URLs.',
    author='Tomas Pedros',
    install_requires = (['streamlit', 'streamlit_extras.app_logo', 'streamlit_option_menu', 'io', 'openpyxl', 'openpyxl.styles', 'csv', 'pyperclip']),
    packages=find_packages(include = ["Streamlit_UTM_genie"]),
)

