import streamlit as st
import pandas as pd
from streamlit_card import card
import math

st.set_page_config(layout="wide")

input_text = st.session_state["input_text"]
image_switch = st.session_state["image_switch"]
# st.text(input_text)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
        }
        .stText {
            text-align:center;
            justify-content:center;
            align-items:center;
            font-size: 5rem;
            font-weight: bold;
        }
    </style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    df = pd.read_csv(r"./moviename.csv", index_col=False)
    return df


def create_card(title, text, image_url, styles, on_click=None, key=None):
    return card(
        title=title,
        text=text,
        image=image_url,
        styles=styles,
        on_click=on_click,
        key=key,
    )


st.session_state["card_clicked"] = None


def on_card_click(card_index):
    st.session_state["card_clicked"] = card_index
    st.switch_page("pages/3_Review.py")


# st.markdown('<div class="center">CineScore</div>', unsafe_allow_html=True)
st.text("Pick Your Movie")


df = load_data()

search_df = df[df["primaryTitle"].str.contains(input_text, case=False, na=False)]
search_tconst = search_df["tconst"].tolist()
search_title = search_df["primaryTitle"].tolist()
search_year = search_df["startYear"].tolist()
imagelink = None
search_length = len(search_df)

# st.write(search_df)
# st.text(search_length)

st.session_state["search_df"] = search_df

no_of_rows = math.ceil(search_length / 4)


i = 0
for j in range(no_of_rows):
    cols = st.columns(4)
    for col in cols:
        if i < search_length:
            if search_year[i] == "\\N":
                search_year[i] = "NA"
            if image_switch:
                imagelink = (
                    f"https://img.omdbapi.com/?i={search_tconst[i]}&apikey=49d8e04d"
                )
            with col:
                on_click_function = lambda i=i: on_card_click(i)
                create_card(
                    title=search_title[i],
                    text=search_year[i],
                    image_url=imagelink,
                    on_click=on_click_function,
                    key=f"{i}",
                    styles={
                        "card": {
                            "width": "300px",
                            "height": "420px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                        },
                        "text": {
                            "font-family": "serif",
                        },
                    },
                )
        i += 1
