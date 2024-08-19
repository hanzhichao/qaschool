import requests
from bs4 import BeautifulSoup


url = "http://www.testtao.cn/?p=3100"

res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, features="lxml")
for i in soup.find("div",class_='entry-content clearfix').find_all("a"):
	print(i.text)
	print(i.attrs['href'])


res2 = requests.get("http://www.testtao.cn/?p=2983")
soup2 = BeautifulSoup(res2.text, features="lxml")
print(soup2.find("div",class_='entry-content clearfix'))