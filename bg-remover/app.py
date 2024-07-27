from flask import Flask, request, send_file, render_template, redirect, url_for, jsonify
from rembg import remove
from PIL import Image
import os
import uuid

app = Flask(__name__)

# Define input and output folders
INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

# Ensure the folders exist
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_name = f"{uuid.uuid4().hex}_{file.filename}"
        input_file_path = os.path.join(INPUT_FOLDER, file_name)
        file.save(input_file_path)

        # Extract the file extension and format
        file_extension = file.filename.rsplit('.', 1)[1].lower()
        output_file_name = f"{uuid.uuid4().hex}.{file_extension}"
        output_file_path = os.path.join(OUTPUT_FOLDER, output_file_name)

        try:
            with Image.open(input_file_path) as image:
                # Remove the background
                output_image = remove(image)

                # Check the file extension and adjust mode if needed
                if file_extension in ['jpg', 'jpeg']:
                    if output_image.mode == 'RGBA':
                        # Convert RGBA to RGB for JPEG
                        output_image = output_image.convert('RGB')
                    output_image.save(output_file_path, format='JPEG')
                elif file_extension == 'png':
                    output_image.save(output_file_path, format='PNG')
                else:
                    return jsonify({'error': 'Unsupported file format'}), 400
            
            # Redirect to the URL for downloading the image
            return redirect(url_for('download_image', filename=output_file_name))
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    else:
        return jsonify({'error': 'Invalid file format'}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_image(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    # Return the file for viewing
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True,port=7777)
