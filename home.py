import streamlit as st
from helper import download_stopwords


st.set_page_config(layout="centered")
input_text = None
submit_button = None
st.session_state["image_switch"] = None
download_stopwords

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
        }

        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 10vh;
            text-align: center;
        }

        .stText {
            text-align: center;
            font-size: 6rem;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .stContainer{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align:center;
            width:100%;
        }

        .stForm {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align:center;
            border:none;
            outline:none;
            width:100%;
        }

        .stForm .stButton{
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .stTextInput {
            display: flex;
            justify-content: center;
            align-items: center;
            width:500px;
        }
        .stTextInput input:focus {
            border: none !important;
            outline: none !important;
        }

        .stTextInput, .stButton {
            border: none;
            outline: none;
        }

        .stFormSubmitButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }

        .stFormSubmitButton button:hover {
            background-color: #45a049;
            color:white;
            border-color: green;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Display "CineScore" text with custom styling
    st.markdown('<div class="stText">CineScore</div>', unsafe_allow_html=True)
    with st.form(key="user_input_text", enter_to_submit=True, border=False):
        input_text = st.text_input(
            "", key="movie_input", placeholder="Enter Your Favourite Movie Name"
        )
        st.markdown('<div class="stForm">', unsafe_allow_html=True)
        submit_button = st.form_submit_button()

        image_switch = st.toggle("Show Poster")
        if image_switch:
            st.session_state["image_switch"] = 1

        if submit_button:
            if not input_text:
                st.warning("Please Insert Movie Name")
            else:
                st.session_state["input_text"] = input_text
                st.switch_page("pages/2_Suggestions.py")

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
