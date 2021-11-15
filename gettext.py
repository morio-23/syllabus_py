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

gakubu_head = ["10","11","90","13","14","16","17","18","19"]
gakubu_end = ["91","10","20","30","40","60","7050","80","90"]

#医学部以外
for j in range(9):
    while(i < 10000):
        pdfurl = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/"+gakubu_head[j]+ str(i).zfill(4) +gakubu_end[j]+"_syllabus.pdf"
        print(pdfurl)
        res = requests.get(pdfurl)
        print(res.status_code)
        if(res.status_code != 404):
            url = "http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd="+gakubu_head[j]+ str(i).zfill(4) +gakubu_end[j]+"&val_year=2021"
            print(url)
            res = requests.get(url)
            print(res.status_code)
            if(res.status_code != 404):
                filename = gakubu_head[j] + str(i).zfill(4) + ".txt"
                #どの環境でもpdffileの絶対パスを取得して保存する
                filepath = os.path.join(file_path, filename)
                soup = bs4.BeautifulSoup(res.content, "html.parser")
                text = soup.get_text()
                fw = open(filepath,'w', encoding="UTF-8")
                fw.write(text)
                fw.close()
        i = i+1
    i=0

#医学部
while(i < 10000):
    pdfurl_igakuka = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/15"+ str(i).zfill(4)+"5015_syllabus.pdf"
    pdfurl_kango = "http://syllabus.adm.u-toyama.ac.jp/syllabus/formatter/pdf/15"+ str(i).zfill(4)+"5010_syllabus.pdf"
    print(pdfurl_igakuka)
    res_igaku = requests.get(pdfurl_igakuka)
    print(res_igaku.status_code)
    print(pdfurl_kango)
    res_kango = requests.get(pdfurl_kango)
    print(res_kango.status_code)
    if(res_igaku.status_code != 404 and res_kango.status_code == 404):
        end = "5010"
        getdata = True
    elif(res_igaku.status_code == 404 and res_kango.status_code != 404):
        end = "5015"
        getdata = True
    elif(res_igaku.status_code != 404 and res_kango.status_code != 404):
        getdata = False
        print("医学科・看護学科どちらもリンクが存在します\n")
    else:
        getdata = False
    if(getdata):
        url = "http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=15"+ str(i).zfill(4) +end+"&val_year=2021"
        print(url)
        res = requests.get(url)
        print(res.status_code)
        if(res.status_code != 404):
            filename = "15" + str(i).zfill(4) + ".txt"
            print(filename+"\n")
            #どの環境でもpdffileの絶対パスを取得して保存する
            filepath = os.path.join(file_path, filename)
            soup = bs4.BeautifulSoup(res.content, "html.parser")
            text = soup.get_text()
            fw = open(filepath,'w', encoding="UTF-8")
            fw.write(text)
            fw.close()
    i = i+1


'''
以下各リンク
教養教育　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=10****91&val_year=2021
人文学部　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=11****10&val_year=2021
人間発達科学部　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=90****20&val_year=2021
経済学部　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=13****30&val_year=2021
理学部　　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=14****40&val_year=2021
※医学部は医学科と看護で末尾が違うので両方検索
医学部看護学科　　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=15****5015&val_year=2021
医学部医学科　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=15****5010&val_year=2021
薬学部　　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=16****60&val_year=2021
工学部　　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=17****7050&val_year=2021
芸術文化学部　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=18****80&val_year=2021
都市デザイン学部　http://syllabus.adm.u-toyama.ac.jp/syllabus/search/details.asp?renban_cd=19****90&val_year=2021
'''