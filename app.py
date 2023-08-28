import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

UPLOAD_DIR = 'uploaded_files'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app.config['UPLOAD_DIR'] = UPLOAD_DIR

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_handler():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        filename = uploaded_file.filename
        filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
        uploaded_file.save(filepath)
        return jsonify({"message": "File upload successful"})
    else:
        return jsonify({"error": "No file uploaded"})

@app.route('/get_file_info', methods=['POST'])
def file_info():
    uploaded_files = request.files
    if 'file' not in uploaded_files:
        return jsonify({'error': 'No file part'})

    uploaded_file = uploaded_files['file']
    filename = uploaded_file.filename
    filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
    
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath)  # Get file size in bytes
        file_info = {
            'file_name': filename,
            'file_size_bytes': file_size,
            'file_size_human_readable': _format_size(file_size)
        }
        return jsonify(file_info)
    else:
        return jsonify({'error': 'File not found'})

def _format_size(size):
    # Convert bytes to a more human-readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"

if __name__ == '__main__':
    app.run(debug=True)
