import requests
from bs4 import BeautifulSoup

URL= "https://mayonnaiseburger.com/mayonnaiseburger"
page= requests.get(URL)

soup= BeautifulSoup(page.content,"html.parser")
result= soup.find(id="products")

food= result.find_all("p",class_="w3-bold w3-text-gray")
price= result.find_all("div",class_="amount")

print("                                 BURGER MYJ")

for a in range(0,23):
    if a == 0 :
       print("BURGER :")
    elif a == 15 :
        print("SAUCE :")
    print("",food[a].text)
    print("",price[a].text)





