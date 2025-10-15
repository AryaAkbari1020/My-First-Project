import requests
from bs4 import BeautifulSoup

url=requests.got("https://www.tgju.org")
txt=url.text


soup= BeautifulSoup(txt,"html.parser")
tala=soup.find(id="l-mesghal")

output=tala.find(class_="info-price")
print(f"مثقال طلا:{output.txt}")
