import glob
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

#PDFファイルの一覧を取得
pdffiles = glob.glob("pdffile/*.pdf")
print(pdffiles)

manager = PDFResourceManager()

#保存先ファイルの指定・確認してなければ作成
txtfile_path = os.path.abspath('./txtfile')
if os.path.exists(txtfile_path) != True:
    os.mkdir(txtfile_path)

for file in pdffiles:
    pdf_path = file
    output_path = os.path.join(txtfile_path, os.path.split(file)[1] + "_output.txt")
    with open(output_path, "wb") as output:
        with open(pdf_path, 'rb') as input:
            with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
                interpreter = PDFPageInterpreter(manager, conv)
                for page in PDFPage.get_pages(input):
                    interpreter.process_page(page)


