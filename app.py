import streamlit as st
import random

st.set_page_config(page_title="AI Brand Tweet Generator", page_icon="🐦", layout="wide")

st.title("🐦 AI Brand Tweet Generator")
st.write("Generate a **Brand Summary** and **10 marketing tweets** for your brand.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    brand = st.text_input("Brand Name")
    industry = st.text_input("Industry")
    goal = st.text_input("Tweet Goal (Promotion, Awareness, Launch etc.)")

with col2:
    description = st.text_area("Brand Description")
    tone = st.selectbox(
        "Tweet Tone",
        ["Professional", "Playful", "Bold", "Inspirational", "Casual"]
    )

st.divider()

generate = st.button("🚀 Generate Tweets")

if generate:
    if not brand or not industry or not goal or not description:
        st.warning("Please fill all fields.")
    else:
        # Brand summary generation
        audiences = [
            "young professionals",
            "tech enthusiasts",
            "fitness lovers",
            "creative entrepreneurs",
            "modern lifestyle seekers"
        ]

        themes = [
            "innovation",
            "community engagement",
            "product benefits",
            "lifestyle inspiration",
            "customer success"
        ]

        audience = random.choice(audiences)

        st.subheader("📊 Brand Summary")

        st.markdown(f"""
**Tone:** {tone}  
**Target Audience:** {audience} interested in {industry}  
**Content Themes:** {themes[0]}, {themes[1]}, {themes[2]}, {themes[3]}
""")

        st.subheader("🐦 Generated Tweets")

        tweet_templates = [
            f"{brand} is changing the {industry} game. Stay ahead with us! #{brand} #{industry}",
            f"Big things are happening at {brand}. Join the movement! #{brand} #Innovation",
            f"Ready for the future of {industry}? {brand} has you covered. #{brand}",
            f"Experience the power of {brand}. Built for people who love {industry}. #{brand}",
            f"{brand} brings fresh energy to {industry}. Let’s grow together. #{brand}",
            f"Smarter. Better. Faster. That’s the {brand} way. #{brand}",
            f"Your journey in {industry} starts with {brand}. #{brand}",
            f"Discover what makes {brand} different in the world of {industry}. #{brand}",
            f"Innovation meets passion at {brand}. #{brand} #{industry}",
            f"The future of {industry} is here with {brand}. #{brand}"
        ]

        random.shuffle(tweet_templates)

        for i in range(10):
            st.write(f"{i+1}. {tweet_templates[i]}")
