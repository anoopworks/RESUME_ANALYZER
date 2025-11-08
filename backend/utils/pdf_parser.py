import pdfplumber
from typing import Optional

def extract_text_from_pdf(pdf_file_path: str) -> Optional[str]:
    """
    Extracts text content from a PDF file.

    Args:
        pdf_file_path: The path to the uploaded PDF file.

    Returns:
        The extracted text content as a string, or None if extraction fails.
    """
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        
        # Simple Preprocessing Unit implementation: remove excessive whitespace/empty lines
        clean_text = "\n".join(filter(str.strip, text.splitlines()))
        
        return clean_text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
        