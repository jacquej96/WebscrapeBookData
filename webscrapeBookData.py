import bs4, requests

page = requests.get('https://www.librarything.com/z_books.php')
page.raise_for_status()
    
file = open('books.php', 'wb')
for chunk in page.iter_content(100000):
    file.write(chunk)
file.close()
