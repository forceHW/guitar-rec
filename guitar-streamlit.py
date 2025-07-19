import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('API_KEY'))

st.title("Electric Guitar Recommender")

with st.form("guitar_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        min_budget = st.text_input("Min Budget", placeholder="Enter min budget")
    with col2:
        max_budget = st.text_input("Max Budget", placeholder="Enter max budget")
    
    genre = st.selectbox(
        "Choose a Genre/Tone",
        ["I Don't Know", "Heavy Metal", "Hard Rock", "Jazz", "Blues", "Funk", "Country"]
    )
    
    shape = st.text_input("Preferred Shape (leave blank if none)", placeholder="e.g., Stratocaster")
    
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    if not min_budget or not max_budget:
        st.warning("Please enter both budget values")
    else:
        with st.spinner("Finding the perfect guitars for you..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "In response to the user, display a list of about 10-20 guitars that fit within the given budget. Format each recommendation on a new line with a bullet point."
                    },
                    {
                        "role": "user",
                        "content": f"Can you recommend me a beginner guitar with a budget range of {min_budget} to {max_budget}, "
                                f"for playing {genre} music, and with a preferred shape of '{shape}'?"
                    }
                ],
                model="gpt-4", 
            )

            recommendations = chat_completion.choices[0].message.content
            
            st.subheader("Recommended Guitars:")
            st.markdown(recommendations)