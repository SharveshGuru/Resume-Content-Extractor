# server.py


from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import csv
import extract_from_doc
import extract_from_docx
import extract_from_pdf
import extract_email
import extract_phoneno
import extract_name
import extract_edu

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload', methods=['POST'])
def upload_files():
    
    def add_data_to_csv(file_path, data):
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
        
    if 'resumes' not in request.files:
        return jsonify({'error': 'No files part'})

    files = request.files.getlist('resumes')

    for file in files:
        if file.filename == '':
            continue

        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Process the uploaded file
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        _, ext = os.path.splitext(resume_path)

        if ext in ['.doc', '.docx', '.pdf']:
            if ext == ".docx":
                text = extract_from_docx.extract_text_from_doc(resume_path)
            elif ext == ".doc":
                text = extract_from_doc.extract_text_from_doc(resume_path)
            elif ext == ".pdf":
                text = extract_from_pdf.extract_text_from_pdf(resume_path)
            name = extract_name.extract_name(text)
            email = extract_email.extract_email(text)
            pno = extract_phoneno.extract_phoneno(text)
            edu = extract_edu.extract_education(text)
            print(name, email, pno, edu, sep="\n")
            row = (name, email, pno, edu)
            add_data_to_csv("data.csv", row)

    return jsonify({'message': 'Files uploaded successfully'})

@app.route('/download')
def download_file():
    return send_from_directory('.', 'data.csv', as_attachment=True)

with open("data.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name","Email","Phone No","Education"])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
