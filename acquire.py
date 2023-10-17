# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_blog_articles():
    soup = BeautifulSoup((requests.get('https://codeup.edu/blog/', 
                                   headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"})).text, 'html.parser')
    blog_links = [element['href'] for element in soup.find_all('a', class_='more-link')]
    all_blogs = []
    for link in blog_links:
        soup = BeautifulSoup((requests.get(link, 
                            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"})).text, 'html.parser')
        title = soup.find('h1', class_='entry-title').text
        body = soup.find('div', class_='entry-content').text.strip().replace('\n', ' ')
        row = {'title': title, 'article': body}
        all_blogs.append(row)
    return pd.DataFrame(all_blogs)


def get_news_article():
    base_url = 'https://inshorts.com/en/read/'
    categories = [
    'business',
    'entertainment',
    'technology',
    'sports'
    ]
    all_articles = pd.DataFrame(columns = ['title', 'body', 'category'])
    for category in categories:
        category_url = base_url + category
        cont = requests.get(category_url).text
        soup = BeautifulSoup(cont, 'html.parser')
        title = [element.text for element in soup.find_all('span', itemprop='headline')]
        body = [element.text for element in soup.find_all('div', itemprop='articleBody')]
        cat = pd.DataFrame({'title': title, 'body': body, 'category': category})
        all_articles =pd.concat([all_articles, cat], axis = 0, ignore_index=True)
    return all_articles