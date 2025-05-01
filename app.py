import streamlit as st
from summarizer import split_text, summarize_chunks
from pdf_reader import pdf_to_text

st.title("🧠 Legal Document Summarizer")

uploaded_file = st.file_uploader("Upload a legal judgment (PDF)", type=["pdf"])
length = st.selectbox("Choose summary length", ["brief", "moderate", "detailed"])

if uploaded_file:
    raw_text = pdf_to_text(uploaded_file)
    st.text_area("Original Document", raw_text[:3000], height=300)

    if st.button("Generate Summary"):
        with st.spinner("Processing full document..."):
            chunks = split_text(raw_text, max_tokens=800)
            summary = summarize_chunks(chunks, length)
        st.success("Summary generated!")
        st.text_area("Full Summary", summary, height=300)
        st.download_button("Download Summary", summary, file_name="summary.txt")
