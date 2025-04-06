import streamlit as st
from transformers import pipeline

# Load NLP pipelines
sentiment_pipeline = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")
reply_generator = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="AI Text Assistant", layout="centered")
st.title("🤖 AI Text Assistant")

st.markdown("""
Enter any text and the assistant will:
- Detect **sentiment** (positive / negative / neutral)
- Generate a **short summary**
- Suggest an **automatic reply**
""")

user_input = st.text_area("Enter text:", height=200)

if st.button("Analyze") and user_input.strip():
    with st.spinner("Analyzing..."):
        # Sentiment analysis
        sentiment = sentiment_pipeline(user_input)[0]
        sentiment_label = sentiment['label']
        sentiment_score = sentiment['score']

        # Summarization
        summary = summarizer(user_input, max_length=60, min_length=20, do_sample=False)[0]['summary_text']

        # Auto-reply
        prompt = f"Reply to the following message: {user_input}\nReply:"
        reply = reply_generator(prompt, max_length=80, num_return_sequences=1)[0]['generated_text'].split("Reply:")[-1].strip()

    st.subheader("🔍 Analysis Results")

    st.markdown(f"**Sentiment:** {sentiment_label} ({sentiment_score:.2f})")
    st.markdown(f"**Summary:** {summary}")
    st.markdown(f"**Auto-Reply:** {reply}")

st.markdown("---")
st.caption("Built with ❤️ and 🤍 Hugging Face Transformers")
