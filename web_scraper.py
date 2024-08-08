import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    paragraphs = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])
    
    return article_text

if __name__ == "__main__":
    url = input("Enter the URL of the news article: ")
    html_content = fetch_html(url)
    
    if html_content:
        article_text = parse_html(html_content)
        print(article_text)
