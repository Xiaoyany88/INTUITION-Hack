import PyPDF2

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