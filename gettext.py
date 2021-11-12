from bs4 import BeautifulSoup
import bs4
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin
import os

i = 0

#保存先ファイルの指定・確認してなければ作成
file_path = os.path.abspath('./downloadtxt')
if os.path.exists(file_path) != True:
    os.mkdir(file_path)

#保存先ファイルの指定・確認してなければ作成

while(i < 10000):
    pdfurl = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/17"+ str(i).zfill(4) +"7050_syllabus.pdf"
    print(pdfurl)
    res = requests.get(pdfurl)
    print(res.status_code)
    if(res.status_code != 404):
        url = "http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=17"+ str(i).zfill(4) +"7050&val_year=2021"
        print(url)
        res = requests.get(url)
        print(res.status_code)
        if(res.status_code != 404):
            filename = "17" + str(i).zfill(4) + ".txt"
            #どの環境でもpdffileの絶対パスを取得して保存する
            filepath = os.path.join(file_path, filename)
            soup = bs4.BeautifulSoup(res.content, "html.parser")
            text = soup.get_text()
            fw = open(filepath,'w', encoding="UTF-8")
            fw.write(text)
            fw.close()
    i = i+1
    