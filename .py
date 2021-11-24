#テスト用pyファイルだよ
from bs4 import BeautifulSoup
import bs4
import requests
import urllib
import urllib.request as req
from urllib.parse import urljoin
import os

i = 0

fw = open("edittxt/902120.txt",'r', encoding="UTF-8")
print(fw)
txt = fw.readlines()
print(txt)
fw.close()

