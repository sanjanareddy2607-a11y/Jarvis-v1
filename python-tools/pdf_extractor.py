"""
PDF Text Extractor Tool
Uses PyMuPDF to extract text from PDFs
"""

import fitz  # PyMuPDF

def extract_pdf_text(file_path, max_pages=None):
    """
    Extract text from PDF file
    
    Args:
        file_path: Full path to PDF file
        max_pages: Maximum pages to extract (None = all)
        
    Returns:
        dict with extracted text and metadata
    """
    try:
        pdf_document = fitz.open(file_path)
        
        text_content = ""
        page_count = len(pdf_document)
        
        # Limit pages if specified
        pages_to_read = min(page_count, max_pages) if max_pages else page_count
        
        for page_num in range(pages_to_read):
            page = pdf_document[page_num]
            text_content += f"\n--- Page {page_num + 1} ---\n"
            text_content += page.get_text()
        
        pdf_document.close()
        
        return {
            "success": True,
            "content": text_content,
            "file_path": file_path,
            "total_pages": page_count,
            "pages_extracted": pages_to_read,
            "message": f"Extracted {pages_to_read}/{page_count} pages from PDF"
        }
    
    except FileNotFoundError:
        return {
            "success": False,
            "content": None,
            "error": f"PDF file not found: {file_path}"
        }
    
    except Exception as e:
        return {
            "success": False,
            "content": None,
            "error": f"Error extracting PDF: {str(e)}"
        }


if __name__ == "__main__":
    # Test with a sample PDF
    # Place a test.pdf in jarvis/data/ first
    result = extract_pdf_text(r"C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis\data\test.pdf", max_pages=2)
    print(result)