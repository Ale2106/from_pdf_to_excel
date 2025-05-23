import re
from pypdf import PdfReader

with open ("pdf_to_txt.txt", "a", encoding="utf-8") as f:
    pdf_content = PdfReader("Reti pool domande.pdf")
    data_page = pdf_content.pages
    
    #print(pdf_content.pages)
    """
    page = data_page[0]
    text = page.extract_text()
    text = re.sub(r'(\d+\))', r'\n\1', text)
    print(text)
    """
    
    for page in data_page :
        text = page.extract_text()
        text = re.sub(r'(\d+\))', r'\n\1', text)
        f.write(str(text))
    
    