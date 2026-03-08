import streamlit as st
from openai import OpenAI

# Page title
st.title("AI Brand Tweet Generator")
st.write("Generate engaging tweets for your brand using AI")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# User input
brand = st.text_input("Enter your brand name")

# Button
if st.button("Generate Tweets"):

    if brand == "":
        st.warning("Please enter a brand name")
    else:

        prompt = f"""
        Generate 3 engaging Twitter/X tweets for the brand "{brand}".

        Requirements:
        - Each tweet must be under 280 characters
        - Make them catchy and marketing focused
        - Add relevant hashtags
        - Friendly brand voice
        """

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
