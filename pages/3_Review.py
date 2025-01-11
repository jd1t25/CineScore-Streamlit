import streamlit as st
import pandas as pd
from helper import get_reviews

st.set_page_config(layout="centered")
card_index = st.session_state["card_clicked"]
card_index = 0
# st.text(card_index)
st.session_state["card_clicked"] = None


# input_text = st.session_state["input_text"]
search_df = st.session_state["search_df"]

user_movie = search_df.iloc[card_index]
# st.write(user_movie)

tconst = user_movie["tconst"]
name = user_movie["primaryTitle"]
# st.text(tconst)

reviews = ["hello", "good", "bye"]
user_score = [5, 6, 7]
predicted_score = [1, 2, 3]

# tdf = pd.DataFrame(
#     {"reviews": reviews, "user_score": user_score, "predicted_score": predicted_score}
# )

tdf = get_reviews(tconst)

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
            text-align:center;
            justify-content:center;
            align-items:center;
            font-size: 5rem;
            font-weight: bold;
        }
        .stTable {
            margin-top: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width:900px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Display movie information and review table
    st.markdown('<div class="centertext">', unsafe_allow_html=True)
    st.text(name)
    st.markdown("</div>", unsafe_allow_html=True)
    st.table(tdf)
    # st.dataframe(tdf, use_container_width=True, height=800,hide_index=True)

    home = st.button("Home")
    if home:
        st.switch_page("home.py")
    st.markdown("</div>", unsafe_allow_html=True)
