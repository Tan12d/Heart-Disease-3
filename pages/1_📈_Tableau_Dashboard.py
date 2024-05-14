from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title(":bar_chart: Tableau Dashboard")

# Import your data
heart_data = pd.read_excel("data.xlsx")
pyg_app = StreamlitRenderer(heart_data)
 
pyg_app.explorer()

st.image("chart.png")

_, col2, _ = st.columns(3)

with col2:
    _, col_2, _ = st.columns(3)

    with col_2:
        if st.button("Back to Home 🏠"):
            switch_page("Homepage")