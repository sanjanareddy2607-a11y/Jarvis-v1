"""
Flask Server for Jarvis AI Tools
Exposes Python tools as HTTP APIs
"""

from flask import Flask, request, jsonify
from file_reader import read_text_file
from pdf_extractor import extract_pdf_text
from csv_analyzer import analyze_csv
from file_lister import list_directory
import traceback

# Create Flask app
app = Flask(__name__)

# ===== FILE READING ENDPOINT =====
@app.route('/api/read_file', methods=['POST'])
def read_file_endpoint():
    """
    Read a text file
    
    Request body:
    {
        "file_path": "C:/path/to/file.txt"
    }
    """
    try:
        data = request.json
        file_path = data.get('file_path')
        
        if not file_path:
            return jsonify({'error': 'file_path is required'}), 400
        
        result = read_text_file(file_path)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500


# ===== PDF EXTRACTION ENDPOINT =====
@app.route('/api/extract_pdf', methods=['POST'])
def extract_pdf_endpoint():
    """
    Extract text from PDF
    
    Request body:
    {
        "file_path": "C:/path/to/file.pdf",
        "max_pages": 5
    }
    """
    try:
        data = request.json
        file_path = data.get('file_path')
        max_pages = data.get('max_pages')
        
        if not file_path:
            return jsonify({'error': 'file_path is required'}), 400
        
        result = extract_pdf_text(file_path, max_pages=max_pages)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500


# ===== CSV ANALYSIS ENDPOINT =====
@app.route('/api/analyze_csv', methods=['POST'])
def analyze_csv_endpoint():
    """
    Analyze CSV file
    
    Request body:
    {
        "file_path": "C:/path/to/file.csv"
    }
    """
    try:
        data = request.json
        file_path = data.get('file_path')
        
        if not file_path:
            return jsonify({'error': 'file_path is required'}), 400
        
        result = analyze_csv(file_path)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500


# ===== FILE LISTING ENDPOINT =====
@app.route('/api/list_directory', methods=['POST'])
def list_directory_endpoint():
    """
    List files in a directory
    
    Request body:
    {
        "folder_path": "C:/path/to/folder",
        "max_depth": 2
    }
    """
    try:
        data = request.json
        folder_path = data.get('folder_path')
        max_depth = data.get('max_depth', 2)
        
        if not folder_path:
            return jsonify({'error': 'folder_path is required'}), 400
        
        result = list_directory(folder_path, max_depth=max_depth)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500


# ===== HEALTH CHECK ENDPOINT =====
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Jarvis Python Tools Server is running'}), 200

from resume_analyzer import analyze_resume, match_job_resume

# ===== RESUME ANALYSIS ENDPOINT =====
@app.route('/api/analyze_resume', methods=['POST'])
def analyze_resume_endpoint():
    """
    Analyze a resume PDF
    
    Request body:
    {
        "file_path": "C:/path/to/resume.pdf"
    }
    """
    try:
        data = request.json
        file_path = data.get('file_path')
        
        if not file_path:
            return jsonify({'error': 'file_path is required'}), 400
        
        result = analyze_resume(file_path)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== JOB MATCHING ENDPOINT =====
@app.route('/api/match_job_resume', methods=['POST'])
def match_job_resume_endpoint():
    """
    Match resume with job description
    
    Request body:
    {
        "resume_text": "resume content...",
        "job_description": "job description..."
    }
    """
    try:
        data = request.json
        resume_text = data.get('resume_text')
        job_description = data.get('job_description')
        
        if not resume_text or not job_description:
            return jsonify({'error': 'resume_text and job_description required'}), 400
        
        result = match_job_resume(resume_text, job_description)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ===== START SERVER =====
if __name__ == '__main__':
    print("🚀 Starting Jarvis Python Tools Server...")
    print("📍 Server running on http://localhost:5000")
    print("🔗 Available endpoints:")
    print("   - POST /api/read_file")
    print("   - POST /api/extract_pdf")
    print("   - POST /api/analyze_csv")
    print("   - POST /api/list_directory")
    print("   - GET  /api/health")
    print("\nPress Ctrl+C to stop the server")
    
    app.run(host='localhost', port=5000, debug=True)