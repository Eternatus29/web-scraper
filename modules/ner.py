# Import the spaCy library, which is used for Natural Language Processing (NLP)
import spacy

# Load the pre-trained spaCy model for English language, which will be used for Named Entity Recognition (NER)
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    """
    Extract named entities from the provided text.

    This function uses the spaCy NLP model to identify named entities in the input text.
    Named entities are categorized into different types, such as persons and organizations.
    
    Parameters:
    - text (str): The input text from which named entities will be extracted.

    Returns:
    - dict: A dictionary containing sets of named entities, categorized as 'PERSON' and 'ORG'.
    """
    # Process the text with spaCy to create a Doc object, which contains entity annotations like PERSON, ORG, etc.
    doc = nlp(text)
    
    # Create a dictionary to hold sets of named entities for 'PERSON' and 'ORG' categories
    entities = {
        'PERSON': set(),  # To store names of people
        'ORG': set()      # To store names of organizations
    }
    
    # Iterate over the named entities identified in the text
    for ent in doc.ents:
        # Check if the entity label is one of the categories we're interested in
        if ent.label_ in entities:
            # Add the entity text to the corresponding set in the dictionary
            entities[ent.label_].add(ent.text)
    
    # Return the dictionary containing the extracted entities
    return entities

if __name__ == "__main__":
    # When the script is run directly (not imported), prompt the user for sample text
    sample_text = input("Enter a sample text: ")
    
    # Extract named entities from the provided sample text
    entities = extract_entities(sample_text)
    
    # Print out the extracted named entities in a readable format
    print("Entities extracted:")
    print("Persons:", entities['PERSON'])        # Display names of people found in the text
    print("Organizations:", entities['ORG'])     # Display names of organizations found in the text
