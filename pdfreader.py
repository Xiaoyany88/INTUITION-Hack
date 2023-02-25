import PyPDF2
import re
# Open the PDF file in read-binary mode
with open('Research article sample.pdf', 'rb') as pdf_file:
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Create a string to hold the text extracted from the PDF
    text = ''
    
    # Loop through each page of the PDF
    for page_num in range(len(pdf_reader.pages)):
        
        # Get the page object for the current page
        page = pdf_reader.pages[page_num]
        
        # Extract the text from the page and append it to the string
        text += page.extract_text()
        
# Print the extracted text
print(text)

filename = "output.txt"

with open(filename, mode="w", encoding='utf-8') as file:
    # write text string into file
    file.write(text)

# Read in the text file
with open('output.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# Remove any text in square brackets (e.g. references)
text = re.sub(r'\[[^\]]*\]', '', text)

# Remove any text in curly braces (e.g. metadata)
text = re.sub(r'\{[^\}]*\}', '', text)

# Remove any footnotes
text = re.sub(r'\n\d+\.\s[^\n]*', '', text)

# Remove any URLs or email addresses
text = re.sub(r'\bhttps?:\/\/[^\s]+', '', text)
text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.[\w]+', '', text)

# Remove any remaining punctuation and whitespace
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text)

# Remove metadata
#metadata = re.search(r'(abstract|keywords|introduction)\W[\w\W]*', text, flags=re.I)
#if metadata:
#    text = text.replace(metadata.group(), '')

# Remove any remaining whitespace and newlines
##text = re.sub(r'\s+', ' ', text)

# Save the cleaned text to a new file
with open('cleaned_output.txt', 'w', encoding='utf-8') as f:
    f.write(text)



