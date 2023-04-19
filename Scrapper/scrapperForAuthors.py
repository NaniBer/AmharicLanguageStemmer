
import webbrowser
import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.goodreads.com/list/show/89548.Best_Amharic_Books?page=2'
webbrowser.open(url, new=0, autoraise=True)


res = requests.get(url, verify=False)

soup = BeautifulSoup(res.text, 'html.parser')


links = soup.find_all(class_='authorName')


for link in links:
    webbrowser.open(link['href'])
    res2 = requests.get(link['href'], verify=False)
    page2 = BeautifulSoup(res2.text, 'html.parser')

    # Works for the title
    title = page2.find_all(class_="authorName")
    name = title[0].text
    name.split(',')
    authorDes = page2.find_all(class_="aboutAuthorInfo")
    review = ''
    if authorDes:
        review = authorDes[0].text
    else:
        print("Could not find the h tag with the specified class name")
    if title:
        name = title[0].text
        name = name[1:]
        name = name[:-1]
        print(name)
        file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Authors/{name}.txt"

        if os.path.exists(file_path):
            continue
        else:
            with open(file_path, 'x', encoding="utf-8") as file:
                file.write(review)

    else:
        print("Could not find the h tag with the specified class name")
