"""
Simple file reader tool
Reads TXT, MD, LOG files
"""

def read_text_file(file_path):
    """
    Read a text file and return content
    
    Args:
        file_path: Full path to the text file
        
    Returns:
        dict with content and status
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return {
            "success": True,
            "content": content,
            "file_path": file_path,
            "message": f"Successfully read {file_path}"
        }
    
    except FileNotFoundError:
        return {
            "success": False,
            "content": None,
            "error": f"File not found: {file_path}"
        }
    
    except Exception as e:
        return {
            "success": False,
            "content": None,
            "error": f"Error reading file: {str(e)}"
        }


if __name__ == "__main__":
    # Test the function
    result = read_text_file(r"C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis\README.md")
    print(result)