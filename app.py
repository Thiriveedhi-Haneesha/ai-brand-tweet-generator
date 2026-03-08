import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="AI Brand Tweet Generator",
    page_icon="🐦",
    layout="wide"
)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Title
st.title("🐦 AI Brand Tweet Generator")
st.write("Generate a **brand summary and 10 engaging tweets** instantly.")

st.divider()

# Input layout
col1, col2 = st.columns(2)

with col1:
    brand = st.text_input("Brand Name")
    industry = st.text_input("Industry")
    campaign = st.text_input("Tweet Goal (Promotion, Awareness, Launch etc.)")

with col2:
    description = st.text_area("Brand Description")
    tone = st.selectbox(
        "Tweet Tone",
        ["Professional", "Playful", "Bold", "Inspirational", "Casual"]
    )

st.divider()

generate = st.button("🚀 Generate Tweets")

# Generate tweets
if generate:

    if not brand or not industry or not campaign or not description:
        st.warning("Please fill all fields.")
    else:

        prompt = f"""
        You are an AI social media assistant.

        Brand Name: {brand}
        Industry: {industry}
        Goal: {campaign}
        Brand Description: {description}
        Tone: {tone}

        First create a BRAND SUMMARY including:
        - Tone
        - Target Audience
        - Content Themes (3–5 themes)

        Then generate 10 Twitter/X tweets for this brand.

        Rules:
        - Each tweet under 280 characters
        - Include relevant hashtags
        - Make them engaging and marketing-focused
        - Number tweets from 1 to 10
        """

        with st.spinner("Generating tweets..."):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8
            )

            output = response.choices[0].message.content

        st.success("Tweets Generated!")

        st.subheader("📊 Brand Summary & Tweets")
        st.write(output)
