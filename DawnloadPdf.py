from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin
import os

i = 0

pdffile_path = os.path.abspath('./pdffile')

#保存先ディレクトリが存在しなければ作成する
if os.path.exists(pdffile_path) != True:
    os.mkdir(pdffile_path)

while(i < 10000):
    filename = "17" + str(i).zfill(4) + ".pdf"
    pdfurl = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/17"+ str(i).zfill(4) +"7050_syllabus.pdf"
    print(pdfurl)
    res = requests.get(pdfurl)
    print(res.status_code)
    if(res.status_code != 404):
        #どの環境でもpdffileの絶対パスを取得して保存する
        filepath = os.path.join(pdffile_path, filename)
        req.urlretrieve(pdfurl, filepath)
    i = i+1
    


