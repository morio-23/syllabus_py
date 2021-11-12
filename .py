#テスト用pyファイルだよ
from bs4 import BeautifulSoup
import bs4
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin
import os

i = 0

#保存先ファイルの指定・確認してなければ作成
pdffile_path = os.path.abspath('./dwtxt')
if os.path.exists(pdffile_path) != True:
    os.mkdir(pdffile_path)

filename = "175000.txt"
url = "http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=1750007050&val_year=2021"
print(url)
res = requests.get(url)
print(res.status_code)
if(res.status_code != 404):
    soup = bs4.BeautifulSoup(res.content, "html.parser")
    text = soup.get_text()
    print(text)
    fw = open("maketxt.txt",'w', encoding="UTF-8")
    fw.write(text)
    fw.close()

