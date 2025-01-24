from flask import Flask, request, make_response, jsonify, send_file 
from flask_cors import CORS
import os
from io import BytesIO
from rembg import remove
from PIL import Image

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def main():
    try:
        if 'file' not in request.files:
            return 'test'
        file = request.files['file']
        if file.filename == '':
            return make_response(jsonify({"error": "no file sent"}), 400)
        if file.mimetype not in ['image/jpeg', 'image/jpg', 'image/png']:
            return make_response(jsonify({"error": "unsupported image format"}), 400)
        
        original_img = Image.open(file)
        edited_img = remove(original_img)
        
        img_io = BytesIO()
        edited_img.save(img_io, format='PNG')
        img_io.seek(0)
        
        original_img.close()
        edited_img.close()
        
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "internal server error"}), 500)

if __name__ == '__main__':
    app.run('localhost', 8080, debug=False)
