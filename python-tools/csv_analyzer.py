"""
CSV Analyzer Tool
Reads and analyzes CSV files
"""

import pandas as pd
import json

def analyze_csv(file_path):
    """
    Analyze CSV file and return structure + data
    
    Args:
        file_path: Full path to CSV file
        
    Returns:
        dict with CSV analysis
    """
    try:
        df = pd.read_csv(file_path)
        
        # Get basic info
        rows = len(df)
        columns = list(df.columns)
        
        # Get first 10 rows as preview
        preview = df.head(10).to_dict('records')
        
        # Get data types
        dtypes = df.dtypes.astype(str).to_dict()
        
        return {
            "success": True,
            "file_path": file_path,
            "total_rows": rows,
            "total_columns": len(columns),
            "columns": columns,
            "data_types": dtypes,
            "preview": preview,
            "message": f"Analyzed CSV: {rows} rows, {len(columns)} columns"
        }
    
    except FileNotFoundError:
        return {
            "success": False,
            "error": f"CSV file not found: {file_path}"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"Error analyzing CSV: {str(e)}"
        }


if __name__ == "__main__":
    # Test with a sample CSV
    result = analyze_csv(r"C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis\data\sample.csv")
    print(json.dumps(result, indent=2))