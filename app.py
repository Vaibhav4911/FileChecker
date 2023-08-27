import os
import subprocess
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        filename = uploaded_file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)
        return jsonify({"message": "File uploaded successfully"})
    else:
        return jsonify({"error": "No file uploaded"})

# magic_obj = magic.Magic()

@app.route('/get_file_info', methods=['POST'])
def get_file_info():
    uploaded_files = request.files
    if 'file' not in uploaded_files:
        return jsonify({'error': 'No file part'})

    uploaded_file = uploaded_files['file']
    filename = uploaded_file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if os.path.exists(filepath):
        # file_type = magic_obj.from_file(filepath)
        file_size = os.path.getsize(filepath)  # Get file size in bytes
        file_info = {
            'file_name': filename,
            # 'file_type': file_type,
            'file_size_bytes': file_size,
            'file_size_human_readable': _format_size(file_size)
            # You can add more information here, such as creation/modification dates, etc.
        }
        return jsonify(file_info)
    else:
        return jsonify({'error': 'File not found'})

def _format_size(size):
    # Helper function to convert bytes to a human-readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"

if __name__ == '__main__':
    app.run(debug=True)