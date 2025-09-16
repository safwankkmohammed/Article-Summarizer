import streamlit as st
from newspaper import Article
from transformers import pipeline


st.set_page_config(
    page_title="🌟 Article Summarizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
        color: #333333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 8px;
    }
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 8px;
    }
    .css-1d391kg {
        background-color: #e6f7ff;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

@st.experimental_singleton
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


summarizer = load_model()

def fetch_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text):
    max_chunk_words = 500
    words = text.split()
    summaries = []
    for i in range(0, len(words), max_chunk_words):
        chunk = " ".join(words[i:i + max_chunk_words])
        summary = summarizer(
            chunk,
            max_length=500,
            min_length=200,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])
    final_summary = " ".join(summaries)
    return final_summary

st.title("🌟 Article Summarizer")
st.write("Get concise summaries from long articles easily! 📰✨")

url = st.text_input("👉 Paste Article URL Here", placeholder="https://example.com/article")
text = st.text_area("Or paste article text here", height=200)

if st.button("📄 Generate Summary"):
    if url or text:
        try:
            if url:
                with st.spinner("⏳ Fetching article..."):
                    article_text = fetch_article_text(url)
            else:
                article_text = text

            with st.spinner("📝 Generating summary..."):
                summary = summarize_text(article_text)

            st.subheader("🔹 Summary")
            st.success(summary)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please enter a URL or paste some text!")
