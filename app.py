import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="AI Brand Tweet Generator", page_icon="🐦")

st.title("🐦 AI Brand Tweet Generator")
st.write("Generate engaging marketing tweets for your brand.")

# Initialize OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# User Inputs
brand = st.text_input("Brand Name")
industry = st.text_input("Industry (e.g., Fashion, Tech, Fitness)")
campaign = st.text_input("Campaign Goal (e.g., Product Launch, Sale Promotion)")
description = st.text_area("Brand Description")

# Generate Button
if st.button("Generate Tweets"):

    if not brand or not industry or not campaign or not description:
        st.warning("Please fill in all fields.")
    else:

        prompt = f"""
        Create 3 engaging Twitter/X tweets for a brand.

        Brand Name: {brand}
        Industry: {industry}
        Campaign Goal: {campaign}
        Brand Description: {description}

        Rules:
        - Each tweet must be under 280 characters
        - Use a catchy marketing tone
        - Include relevant hashtags
        - Separate each tweet clearly
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8
            )

            tweets = response.choices[0].message.content

            st.subheader("Generated Tweets")
            st.write(tweets)

        except Exception as e:
            st.error(f"Error: {e}")
