from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url="https://mu.microchip.com/page/all-courses"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
r=urlopen(req)
soup = BeautifulSoup(r, "html.parser")

# print(soup)


# print(soup.prettify(encoding="utf-8"))

y=soup.find_all("div", class_="coursebox-text")
x=soup.find_all("div", class_="coursebox-text-description")
course_dict = {}

for div_text, div_description in zip(x, y):
    text = div_text.get_text(strip=True)
    description = div_description.get_text(strip=True)
    course_dict[description] = text
    
print(course_dict)
