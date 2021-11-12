import glob
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

files = glob.glob("testdir//*.pdf")
print(files)

manager = PDFResourceManager()

for file in files:
    pdf_path = file
    output_path = file + "_output.txt"
    with open(output_path, "wb") as output:
        with open(pdf_path, 'rb') as input:
            with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
                interpreter = PDFPageInterpreter(manager, conv)
                for page in PDFPage.get_pages(input):
                    interpreter.process_page(page)


