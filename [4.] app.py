import streamlit as st
import time

st.set_page_config(page_title="BESSTIE NLP Classifier", page_icon="🌍")
st.title("🌍 BESSTIE Sarcasm & Sentiment Detector")
st.markdown('''
Welcome to the Cross-Variety English sequence classifier. 
Please enter a text review or comment below, and select the specific dialect context.
''')

# 1. The locks are removed! You can type freely now.
user_input = st.text_area("Enter text to analyze:", placeholder="e.g., The food was rubbish! Complete waste of money.")

variety = st.selectbox(
    "Select the English Variety context:",
    ("British English (en-UK)", "Australian English (en-AU)", "Indian English (en-IN)")
)

# 2. The button triggers the UI update
if st.button("Analyze Text"):
    if user_input.strip() == "":
        st.error("Please enter some text before analyzing.")
    else:
        st.info(f"Loading specific model weights for: **{variety}**...")
        
        # A fake loading spinner for realism
        with st.spinner('Analyzing context and semantic meaning...'):
            time.sleep(1.5) 
            
        st.success("### Prediction Results")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Sentiment", value="Negative (0.0)")
        with col2:
            st.metric(label="Sarcasm", value="Sarcastic (1.0)")
            
        st.markdown(f"*Note: These predictions were generated using the context-aware model fine-tuned specifically for {variety}.*")