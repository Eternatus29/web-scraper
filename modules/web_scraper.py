# Import necessary libraries for web scraping
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetch the HTML content of a web page given its URL.

    This function performs an HTTP GET request to retrieve the page content.
    If the request is successful (status code 200), it returns the HTML content.
    Otherwise, it raises an exception with the status code of the failed request.
    
    Parameters:
    - url (str): The URL of the web page to fetch.

    Returns:
    - str: The HTML content of the web page if the request is successful.
    - None: If an error occurs or the request fails.
    """
    try:
        # Perform an HTTP GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the HTML content of the page
            return response.text
        else:
            # Raise an exception if the request failed
            raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")
    
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {e}")
        # Return None to indicate failure
        return None

def parse_html(html_content):
    """
    Parse the HTML content and extract text from all paragraph elements.

    This function uses BeautifulSoup to parse the provided HTML content
    and extract the text from all <p> (paragraph) tags, combining them into a single string.
    
    Parameters:
    - html_content (str): The HTML content of the web page.

    Returns:
    - str: A concatenated string of all paragraph texts extracted from the HTML.
    """
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <p> tags in the HTML content
    paragraphs = soup.find_all('p')
    
    # Extract the text from each <p> tag and join them into a single string
    article_text = ' '.join([p.get_text() for p in paragraphs])
    
    # Return the combined text from all paragraphs
    return article_text

if __name__ == "__main__":
    """
    Main script execution for fetching and parsing web page content.
    
    When the script is run directly, it prompts the user to enter a URL,
    fetches the HTML content of the web page, parses it to extract text from
    paragraph elements, and then prints the extracted text.
    """
    # Prompt the user to enter the URL of the news article
    url = input("Enter the URL of the news article: ")
    
    # Fetch the HTML content from the provided URL
    html_content = fetch_html(url)
    
    if html_content:
        # Parse the HTML content to extract text from paragraphs
        article_text = parse_html(html_content)
        # Print the extracted article text
        print(article_text)
