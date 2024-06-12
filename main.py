import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set Streamlit app title and description
st.title("🎶 Audio Summary Generator 🎶")
st.write("Upload an audio file and get a brief summary using Google's Generative AI. Let's make it fun and informative! 😃")

# File uploader widget
uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"], accept_multiple_files=False)

# Process the uploaded file
if uploaded_file is not None:
    st.write("📝 **Processing your audio file...** Please wait a moment. ⏳")

    # Save uploaded file to a temporary location
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Upload the file to Google Generative AI
    your_file = genai.upload_file(path=uploaded_file.name)

    # Define the prompt
    prompt = "Listen carefully to the following audio file. Provide a brief summary."

    # Generate content using the model
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content([prompt, your_file])

    # Display the response
    if response:
        st.write("✨ **Here is the summary of your audio file:**")
        # Convert response to simple text
        response_text = response.text if hasattr(response, 'text') else str(response)
        st.success(response_text)
    else:
        st.error("Failed to generate a summary. Please try again with a different audio file.")

# Add some footer information
st.write("🔍 This application uses Google Generative AI to provide summaries of audio content. Your data is processed securely. 🤖")
st.write("Made with ❤️ by Sathyam")
