import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page

# st.set_page_config(layout="wide")


st.header(":mailbox: Get In Touch With me!")



contact_form = """
<form action="https://formsubmit.co/tanmoy234am@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Enter your name" required>
     <input type="email" name="email" placeholder="Enter your email" required>
     <textarea name="message" placeholder="Enter your suggestion"></textarea>
     <button type="submit">Send</button>
</form>
"""



def local_css(file_name):
    """
    Function to apply local CSS styles to a Streamlit app.
    """
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the CSS file relative to the script directory
    css_path = os.path.join(script_directory, file_name)
    
    # Apply local CSS
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("sty.css")

def load_lottiefile(filepath: str):

    json_directory = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(json_directory, filepath)

    with open(json_path, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding = load_lottiefile("lottieimg.json")

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")


col1, col2 = st.columns([2, 3])  # Adjust the width ratio as needed

# Display the second Lottie animation in the second column
# with col1:
#     st_lottie(lottie_hello, key="hello")

# # Display the form in the first column
# with col2:
#     with stylable_container(
#         key="container_with_border",
#         css_styles=[
#             """
#             {   
#                 height:1vw;
#                 top:13vh;
#             }
#             """,
#         ],
#     ):
#         st.markdown(contact_form, unsafe_allow_html=True)



# # JavaScript to trigger the toast message
# st.markdown(
#     """
#     <script>
#     function showToast() {
#         st.toast("Message sent!", "📬")
#     }
#     </script>
#     """,
#     unsafe_allow_html=True
# )

# with stylable_container(
#     key="container",
#     css_styles=[
#         """
#         {   
#             left:12vw;
#             top:-7vh;
#         }
#         """,
#     ],
# ):
#     st_lottie(
#         lottie_coding,
#         speed=1,
#         reverse=False,
#         loop=True,
#         quality="high", # medium ; high
#         height=1200,
#         width=1000,
#         key=None,
#     )

# time.sleep(3)
# st.balloons()


# -----

with col1:
    st_lottie(lottie_hello, key="hello")

# Display the form in the first column
with col2:
    # Render the contact form
    
    st.markdown(contact_form, unsafe_allow_html=True)


# JavaScript to trigger the toast message


st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=None,
    width=None,
    key=None,
)

time.sleep(5)
st.balloons()   

_, col2, _ = st.columns(3)

with col2:
    if st.button("Back to Home 🏠"):
        switch_page("Homepage")