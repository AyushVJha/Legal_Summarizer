# pdf_reader.py
import fitz  # PyMuPDF

def pdf_to_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text
