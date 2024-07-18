import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_option_menu import option_menu

# streamlit run UTM_genie_pages.py

# ------------------------------------------------------------------------------------------------------------------------------

#add_logo("240x240.jpg", height=300)
#st.logo("240x240.jpg")

st.set_page_config(layout="wide")
URL_page = st.Page("Fast_URL_checker.py", title = "Fast URL checker", icon = "")
archivo_URLs_page = st.Page("URLs_via_file.py", title = "URLs via file", icon = "📄")
URL_parameters_creator_page = st.Page("URL_parameters_creator.py", title = "URL parameters creator")
#UTM_Table_page = st.Page("UTM_Campaign_Builder.py", title = "UTM Campaign Builder")

#pg = st.navigation([URL_page, archivo_URLs_page, URL_parameters_creator_page, UTM_Table_page])
pg = st.navigation([URL_page, archivo_URLs_page, URL_parameters_creator_page])
pg.run()


#st.set_page_config(layout="wide")
#add_logo("240x240.jpg", height=300)

#with st.sidebar:
#    selection = option_menu("Menu", ["Fast URL checker", "URLs via file", "URL parameters creator", "UTM Campaign Builder"], 
                            icons=['dash', 'file-earmark',  "dash", "dash"], menu_icon="menu-button-fill", default_index=0)

# Cargar la página seleccionada
#if selection == "Fast URL checker":
#    import Fast_URL_checker

#elif selection == "URLs via file":
#    import URLs_via_file
    
#elif selection == "URL parameters creator":
#    import URL_parameters_creator

#elif selection == "UTM Campaign Builder":
#    import UTM_Campaign_Builder
