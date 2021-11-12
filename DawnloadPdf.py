from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin
import os

i = 0

while(i < 10000):
    filename = "17" + str(i).zfill(4) + ".pdf"
    pdfurl = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/17"+ str(i).zfill(4) +"7050_syllabus.pdf"
    print(pdfurl)
    res = requests.get(pdfurl)
    print(res.status_code)
    if(res.status_code != 404):
        fileurl = os.path.join(os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'pytest'), 'testdir'), filename)
        req.urlretrieve(pdfurl, fileurl)
    i = i+1
    


