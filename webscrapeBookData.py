import bs4, requests

page = requests.get('https://www.librarything.com/z_books.php')
page.raise_for_status()
    
