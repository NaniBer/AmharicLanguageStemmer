
import webbrowser
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/list/show/89548.Best_Amharic_Books?page=2'
webbrowser.open(url, new=0, autoraise=True)


res = requests.get(url, verify=False)

soup = BeautifulSoup(res.text, 'html.parser')


links = soup.find_all(class_='bookTitle')
print(links.count)
for link in links:
    webbrowser.open('www.goodreads.com/'+link['href'])

    res2 = requests.get('https://www.goodreads.com'+link['href'], verify=False)
    page2 = BeautifulSoup(res2.text, 'html.parser')

    # Works for the title

    bookDes = page2.find_all(class_="Formatted")

    review = ''
    if bookDes:
        review = bookDes[0].text
    else:
        print("Could not find the h tag with the specified class name")

    title = page2.title.text
    title = title[:-12]
    title = re.sub(r'[^\w\s]', '', title)
    file_path = f"C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Books/{title}.txt"
    with open(file_path, 'x', encoding="utf-8") as file:
        file.write(review)
