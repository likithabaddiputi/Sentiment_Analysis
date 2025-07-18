import streamlit as st
from main import clean_text, analyse_sentiment, classify_sentiment

st.title("Sentiment Analysis Web App")
st.write("This app analyzes sentiment using NLTK VADER and shows scores with emojis.")

# --- State to store results for Clear button ---
if 'scores' not in st.session_state:
    st.session_state.scores = None
if 'sentiment' not in st.session_state:
    st.session_state.sentiment = None
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

def analyze_text(text):
    cleaned = clean_text(text)
    scores = analyse_sentiment(cleaned)
    sentiment = classify_sentiment(scores)
    st.session_state.scores = scores
    st.session_state.sentiment = sentiment
    st.session_state.input_text = text

# --- Text Input or File Upload ---
uploaded_file = st.file_uploader("Upload a .txt file for analysis (or enter text below)", type=['txt'])

if uploaded_file is not None:
    # Read file content as text
    file_text = uploaded_file.read().decode("utf-8")
    st.text_area("Uploaded file content:", value=file_text, height=150)
    if st.button("Analyze Uploaded Text"):
        analyze_text(file_text)
else:
    text_input = st.text_area("Enter your text here:", value=st.session_state.input_text, height=150)
    if st.button("Analyze Text"):
        if text_input.strip():
            analyze_text(text_input)
        else:
            st.warning("Please enter some text or upload a .txt file!")

if st.session_state.scores is not None:
    # Display sentiment with markdown + emojis
    st.subheader("Sentiment Result")
    st.markdown(f"### {st.session_state.sentiment}")

    # Display VADER scores as JSON
    st.subheader("VADER Scores")
    st.json(st.session_state.scores)

    # Visualize scores with a bar chart (neg, neu, pos)
    scores_chart_data = {
        'Negative': st.session_state.scores['neg'],
        'Neutral': st.session_state.scores['neu'],
        'Positive': st.session_state.scores['pos']
    }
    st.subheader("Sentiment Score Visualization")
    st.bar_chart(scores_chart_data)

    # Clear button to reset
    if st.button("Clear / Try Another"):
        st.session_state.scores = None
        st.session_state.sentiment = None
        st.session_state.input_text = ""
        # Also clear file uploader — reload page recommended
