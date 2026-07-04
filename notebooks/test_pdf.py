from app.parser.pdf_reader import extract_text_from_pdf

pdf_path = "data/raw/sample.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:1000])