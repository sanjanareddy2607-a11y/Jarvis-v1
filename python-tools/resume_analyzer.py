"""
Resume Analyzer Tool
Extracts and analyzes resume content
"""

import json
from pdf_extractor import extract_pdf_text

def analyze_resume(file_path):
    """
    Analyze a resume PDF and extract key information
    
    Args:
        file_path: Path to resume PDF
        
    Returns:
        dict with extracted resume data
    """
    try:
        # Extract PDF text
        pdf_result = extract_pdf_text(file_path)
        
        if not pdf_result.get('success'):
            return {
                'success': False,
                'error': 'Failed to extract PDF'
            }
        
        resume_text = pdf_result.get('content', '')
        
        # Basic extraction (in real app, use NLP)
        # For now, return structured data
        analysis = {
            'success': True,
            'file_path': file_path,
            'raw_text': resume_text[:500],  # First 500 chars
            'total_length': len(resume_text),
            'message': 'Resume extracted successfully. Use Ollama to analyze content for skills, experience, etc.'
        }
        
        return analysis
    
    except Exception as e:
        return {
            'success': False,
            'error': f'Error analyzing resume: {str(e)}'
        }


def match_job_resume(resume_text, job_description):
    """
    Calculate match between resume and job description
    
    Args:
        resume_text: Resume content
        job_description: Job description text
        
    Returns:
        dict with match analysis
    """
    try:
        # Simple keyword matching
        resume_words = set(resume_text.lower().split())
        job_words = set(job_description.lower().split())
        
        matching_words = resume_words.intersection(job_words)
        match_percentage = (len(matching_words) / len(job_words)) * 100 if job_words else 0
        
        return {
            'success': True,
            'match_percentage': round(match_percentage, 2),
            'matching_keywords': list(matching_words)[:20],
            'message': f'{round(match_percentage, 2)}% match with job description'
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'Error matching resume: {str(e)}'
        }


if __name__ == "__main__":
    # Test
    result = analyze_resume(r"C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis\data\resume.pdf")
    print(json.dumps(result, indent=2))