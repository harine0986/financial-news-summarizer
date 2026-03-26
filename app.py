import streamlit as st
from main import summarize_text

st.set_page_config(page_title="Financial Summarizer", page_icon="💰")

st.title("💰 Financial News Summarizer")
st.markdown("### Paste your financial news below 👇")

text = st.text_area("", height=200)

if st.button("🚀 Summarize"):
    if text.strip() == "":
        st.error("Please enter some text!")
    else:
        summary = summarize_text(text, top_n=3)
        st.success("✅ Summary Generated")
        
        for i, line in enumerate(summary, 1):
            st.write(f"{i}. {line}")