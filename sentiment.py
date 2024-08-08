from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

def load_model_and_tokenizer():
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = DistilBertForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def analyze_sentiment(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class_idx = torch.argmax(logits, dim=1).item()
    
    labels = ['negative', 'positive']
    sentiment_label = labels[predicted_class_idx]
    
    return sentiment_label

def main():
    tokenizer, model = load_model_and_tokenizer()
    
    user_input = input("Enter a text for sentiment analysis: ")
    
    sentiment = analyze_sentiment(user_input, tokenizer, model)
    
    print(f"\nSentiment: {sentiment}")

if __name__ == "__main__":
    main()
