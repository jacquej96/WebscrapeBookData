import bs4, requests

page = requests.get('https://www.librarything.com/z_books.php')
page.raise_for_status()

filename = 'books.php'
with open(filename, 'wb') as file:
    for chunk in page.iter_content(100000):
        file.write(chunk)

with open(filename, encoding='utf-8') as file:
    soupFile = bs4.BeautifulSoup(file, "html.parser")
    data = soupFile.select('td[width="60%"] li')
