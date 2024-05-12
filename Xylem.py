from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url="https://mu.microchip.com/page/all-courses"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
r=urlopen(req)
soup = BeautifulSoup(r, "html.parser")

# print(soup)


# print(soup.prettify(encoding="utf-8"))

y=soup.find_all("div", class_="coursebox-text")
listt=[]
for div in y:
    div_text = div.get_text(strip=True)
    listt.append(div_text)
print(listt)