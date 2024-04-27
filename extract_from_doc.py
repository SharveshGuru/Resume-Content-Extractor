from docx import Document

def extract_text_from_doc(docx_file):
    doc = Document(docx_file)
    text = doc.text
    return text
