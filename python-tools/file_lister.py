"""
File Lister Tool
Lists files and folders in a directory
"""

import os

def list_directory(folder_path, max_depth=2):
    """
    List all files and folders in a directory
    
    Args:
        folder_path: Path to folder to list
        max_depth: Maximum folder depth to traverse
        
    Returns:
        dict with file structure
    """
    try:
        file_structure = []
        
        for root, dirs, files in os.walk(folder_path):
            # Calculate current depth
            depth = root.replace(folder_path, '').count(os.sep)
            
            if depth > max_depth:
                continue
            
            # Add folder info
            indent = " " * (depth * 2)
            file_structure.append(f"{indent}📁 {os.path.basename(root)}/")
            
            # Add files
            for file in files[:20]:  # Limit files per folder
                file_structure.append(f"{indent}  📄 {file}")
        
        return {
            "success": True,
            "folder_path": folder_path,
            "structure": "\n".join(file_structure),
            "message": "Successfully listed directory structure"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"Error listing directory: {str(e)}"
        }


if __name__ == "__main__":
    result = list_directory(r"C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis", max_depth=2)
    print(result["structure"])