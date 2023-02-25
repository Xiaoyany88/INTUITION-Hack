# tokenization library
import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Process a sentence
text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)

# Print the individual tokens
for token in doc:
    print(token.text)
