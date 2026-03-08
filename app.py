import streamlit as st
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Brand Tweet Generator")

brand_name = st.text_input("Brand Name")
industry = st.text_input("Industry")
objective = st.selectbox(
    "Campaign Objective",
    ["Engagement", "Promotion", "Awareness"]
)

product_info = st.text_area("Product Description")

if st.button("Generate Tweets"):

    prompt = f"""
Analyze this brand and generate tweets.

Brand Name: {brand_name}
Industry: {industry}
Objective: {objective}
Product: {product_info}

Step 1:
Give 3 bullet points describing brand voice.

Step 2:
Generate 10 tweets matching that tone.
"""

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.8
)
    result = response['choices'][0]['message']['content']

    st.write(result)

