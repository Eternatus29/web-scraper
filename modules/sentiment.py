# Import necessary libraries
import warnings
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

# Suppress FutureWarnings to avoid cluttering the output with warnings about upcoming changes
warnings.simplefilter(action='ignore', category=FutureWarning)

def load_model_and_tokenizer():
    """
    Load the pre-trained DistilBERT model and tokenizer for sentiment analysis.

    The model used here is fine-tuned for sentiment analysis on English text.
    
    Returns:
    - tokenizer (DistilBertTokenizer): The tokenizer used to convert text into token IDs.
    - model (DistilBertForSequenceClassification): The model used to predict sentiment from token IDs.
    """
    # Specify the model name for DistilBERT fine-tuned for sentiment analysis
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    
    # Load the tokenizer and model from the Hugging Face model hub
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = DistilBertForSequenceClassification.from_pretrained(model_name)
    
    # Return the tokenizer and model
    return tokenizer, model

def analyze_sentiment(text, tokenizer, model):
    """
    Analyze the sentiment of the provided text using the pre-trained DistilBERT model.

    This function tokenizes the input text, runs it through the model, and determines whether
    the sentiment is positive or negative based on the model's output.
    
    Parameters:
    - text (str): The text for which sentiment needs to be analyzed.
    - tokenizer (DistilBertTokenizer): The tokenizer to process the text.
    - model (DistilBertForSequenceClassification): The model to perform sentiment classification.

    Returns:
    - sentiment_label (str): The sentiment label of the text ('positive' or 'negative').
    """
    # Tokenize the input text and convert it into tensors suitable for the model
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    
    # Perform inference with no gradient calculations
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract the logits (raw model outputs) and determine the predicted class index
    logits = outputs.logits
    predicted_class_idx = torch.argmax(logits, dim=1).item()
    
    # Define possible sentiment labels
    labels = ['negative', 'positive']
    
    # Map the predicted class index to the corresponding sentiment label
    sentiment_label = labels[predicted_class_idx]
    
    # Return the predicted sentiment label
    return sentiment_label

if __name__ == "__main__":
    # When the script is run directly (not imported), prompt the user for sample text
    """
    Handle user input and perform sentiment analysis.
    
    It loads the model and tokenizer, gets user input, analyzes the sentiment of the input text,
    and prints the result.
    """
    # Load the pre-trained model and tokenizer
    tokenizer, model = load_model_and_tokenizer()
    
    # Prompt the user to enter text for sentiment analysis
    user_input = input("Enter a text for sentiment analysis: ")
    
    # Analyze the sentiment of the input text
    sentiment = analyze_sentiment(user_input, tokenizer, model)
    
    # Print the result of the sentiment analysis
    print(f"\nSentiment: {sentiment}")