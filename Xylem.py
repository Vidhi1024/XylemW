
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# URL of the website containing the list of courses

url = "https://mu.microchip.com/page/all-courses"

try:
    # Open the URL and read its content
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response:
        html_content = response.read()

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all links to individual course pages
    course_links = soup.find_all("a", id_="catalog-courses", class_="course-listing")
    print(course_links,"i")
# //*[@id=]
    # Initialize a dictionary to store course names and their content
    courses_data = {}

    # Iterate through each course link
    for link in course_links:
        # Get the URL of the course page
        course_url = link["href"]

        # Open the course URL and read its content
        req = Request(course_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as course_response:
            course_html_content = course_response.read()

        # Parse the HTML content of the course page
        course_soup = BeautifulSoup(course_html_content, "html.parser")

        # Extract the course name
        course_name = course_soup.find("div", class_="coursebox-text").text.strip()

        # Extract the course content
        course_content = course_soup.find("div", class_="coursebox-text-description").text.strip()

        # Store the course name and content in the dictionary
        courses_data[course_name] = course_content

    # Print the dictionary containing course names and their content
    for course_name, course_content in courses_data.items():
        print("Course Name:", course_name)
        print("Course Content:", course_content)
        print()

except Exception as e:
    print("An error occurred:", e)
