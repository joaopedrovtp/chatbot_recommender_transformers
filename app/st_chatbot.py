import streamlit as st
from streamlit_chat import message as st_message
from random import *
import time
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
from recommender import Recommender


st.set_page_config(
    page_title="Recommendation bot - Streamlit",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:   
    st.write('Hello there! This was developed by Joao Pedro Pereira. Hope you enjoy it :) \n\n If you are looking for more, fell free to ask me: \n\n https://www.linkedin.com/in/joaopedrovtp/')
st.title("Recommendation bot with Streamlit and Transformers")
st.markdown("Check my repository of this project: [Github](https://github.com/joaopedrovtp)")


@st.experimental_singleton
def get_models():
    # it may be necessary for other frameworks to cache the model
    # seems pytorch keeps an internal state of the conversation
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


def recommender(user_message, type_query):
    recommendations = Recommender().recommend(user_message, type_query)
    st.table(recommendations)
    # Update bot message chat history
    st.session_state.history.append({"message": "See my recommendations above! \U0001F917", "is_user": False})    


if "history" not in st.session_state:
    st.session_state.history = []

def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text

    ## Call outsider function - Trigger
    # If user writes 'recommend movie' or '.. series' it calls recommender function
     #   Asks for genre and a detailed description (with an example)
    accepted_strings = {'recommend movie', 'recommend series'}
    clean_message = user_message.strip().lower()
    if clean_message in accepted_strings:
        time.sleep(2)
        words = clean_message.split()
        message_bot = f'Ok, nice! Now please, describe with detailed words the genre(s) and plot of the {words[-1]} you would like to watch. For example: "An action {words[-1]} featuring spaceship battles in a futuristic era"'

        # Save variable of type recommendation (movie/series)
        st.session_state.type_query = words[-1]

        st.session_state.history.append({"message": user_message, "is_user": True, "avatar_style": "pixel-art", "seed": 12})
        st.session_state.history.append({"message": message_bot, "is_user": False})
        
        return 

    # Call the recommender function if is a response from 'recommend movie/series'
    if len(st.session_state.history):
        if 'Ok, nice! Now please, describe with' in st.session_state.history[-1].get('message'): 
            recommender(user_message, st.session_state.type_query)
            return   

    # Response from model
    inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    result = model.generate(**inputs, max_new_tokens= 100)
    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )  # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True,"avatar_style": "pixel-art", "seed": 12}) #"seed": 38
    st.session_state.history.append({"message": message_bot, "is_user": False})

st.text_input("Talk to the bot or type anytime exactly with these words: 'recommend movie' or 'recommend series' ! :robot_face: :movie_camera: :hugging_face:", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat, key=sample(range(100), 10))  # unpacking


