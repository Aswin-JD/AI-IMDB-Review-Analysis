
import streamlit as st

# App Title and Description
st.title('🎥 AI-Based IMDB Movie Review Analyst')
st.subheader('Analyze Movie Reviews Like a Pro!')
st.markdown("""
    Welcome to the **AI-Based IMDB Movie Review Analyst**!  
    This app uses cutting-edge **AI technology** to analyze the sentiment of movie reviews.  
    Enter a review below, and let the AI classify it as **Positive** or **Negative**.  
    Perfect for movie enthusiasts, researchers, and industry professionals! 🍿🎬
""")

# Sidebar for Input Instructions
st.sidebar.header("About This App")
st.sidebar.markdown("""
    This app leverages **Natural Language Processing (NLP)** to understand sentiments in movie reviews.  
    👉 **Instructions**:  
    - Enter an IMDB review in the text box.  
    - Click 'Analyze Sentiment' to see the result.  
    - Explore insights into the review sentiment.
""")

# User Input
review = st.text_area('Enter an IMDB Movie Review:', placeholder="Type your review here...")

# Sentiment Analysis
if st.button('Analyze Sentiment'):
    if review.strip():
        sentiment = classify_comment(review)
        st.success(f"The sentiment of the review is: **{sentiment}**")
    else:
        st.warning('⚠️ Please enter a movie review to analyze.')
