from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

def split_text(text, max_tokens=500):
    paragraphs = text.split('\n\n')
    chunks = []
    current = ""
    for para in paragraphs:
        if len(current) + len(para) < max_tokens:
            current += para + "\n\n"
        else:
            chunks.append(current.strip())
            current = para + "\n\n"
    if current:
        chunks.append(current.strip())
    return chunks

def summarize_chunks(chunks, length="brief"):
    max_len = {"brief": 50, "moderate": 100, "detailed": 200}
    all_summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_len[length], min_length=20, do_sample=False)[0]['summary_text']
        all_summaries.append(summary)
    return "\n\n".join(all_summaries)
