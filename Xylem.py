from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv


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


csv_file_path = "Course_data.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(['Course Name', 'Course Description'])

    for description, text in course_dict.items():
        csv_writer.writerow([description, text])

print("Data written to CSV file successfully!")
