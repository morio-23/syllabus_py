from pdfminer.high_level import extract_text
text = extract_text('11104710_syllabus.pdf')
print(text)