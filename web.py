#importing libraries

import requests
from bs4 import BeautifulSoup

#User Inout from CLI
url = input("Enter the url link to extract : ") 


#Make a get request to fetch the html content of any URL

html_content = requests.get(url).text


#Now Parse the html content to Beutifulsoup4

soup = BeautifulSoup(html_content, 'html.parser')
#print(soup.prettify())

# Filter all javascript, stylesheet and php code
for script in soup(["script", "style", "php"]): # remove all javascript and stylesheet code
    script.extract()
#print(soup.title.text)

#text = soup.find("body").get_text()

# Extract only the text out of URL
text = soup.get_text()

#Print on CLI
print(text)

#Write to text file
with open( r"/home/usama/Documents/Eurus_Tech/Task2_web/Test.txt" ,"w") as oFile:
    oFile.write(str(text))
