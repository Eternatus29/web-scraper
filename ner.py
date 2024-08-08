import spacy

nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    doc = nlp(text)
    
    entities = {
        'PERSON': set(),
        'ORG': set()
    }
    
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].add(ent.text)
    
    return entities

if __name__ == "__main__":
    sample_text = input("Enter a sample text: ")
    entities = extract_entities(sample_text)
    print("Entities extracted:")
    print("Persons:", entities['PERSON'])
    print("Organizations:", entities['ORG'])
