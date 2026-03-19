from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from utils.parser import extract_text
from utils.analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads//Resume.pdf"

# create folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    
    if file:
        filename = secure_filename(file.filename)   # this will be Resume.docx
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        text = extract_text(filepath)
        result = analyze_resume(text)

        return render_template('result.html', result=result)

    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)