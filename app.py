from web_scraper import fetch_html, parse_html
from ner import extract_entities
from sentiment import load_model_and_tokenizer, analyze_sentiment

def main():
    # Get user input
    url = input("Enter the URL of the news article: ")
    
    # Fetch and parse HTML content
    html_content = fetch_html(url)
    
    if html_content:
        article_text = parse_html(html_content)
        print("\nArticle Text:")
        print(article_text)
        
        # Extract entities
        entities = extract_entities(article_text)
        print("\nEntities Extracted:")
        print("Persons:", entities['PERSON'])
        print("Organizations:", entities['ORG'])
        
        # Analyze sentiment
        tokenizer, model = load_model_and_tokenizer()
        sentiment = analyze_sentiment(article_text, tokenizer, model)
        print(f"\nSentiment: {sentiment}")

if __name__ == "__main__":
    main()
