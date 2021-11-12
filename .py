#テスト用pyファイルだよ
import os
pdffile_path = os.path.abspath('./pdffiletest')

if os.path.exists(pdffile_path) != True:
    os.mkdir(pdffile_path)