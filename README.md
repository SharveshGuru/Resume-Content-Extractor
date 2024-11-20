# Resume Content Extractor

A Flask-based web application that extracts key information from resume documents (PDF, DOC, DOCX) including name, email, phone number, and education details.

## Features

- Upload multiple resume documents simultaneously
- Supports PDF, DOC, and DOCX file formats
- Extracts key information:
  - Full Name
  - Email Address
  - Phone Number
  - Education Details
- Exports extracted data to CSV format
- Secure HTTPS connection using SSL certificates
- Web-based interface for easy interaction

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd resume-content-extractor
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download required NLTK and spaCy data:
   ```python
   python -m nltk.downloader stopwords
   python -m spacy download en_core_web_sm
   ```

4. Generate SSL certificates (for HTTPS):
   ```bash
   openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```

## Project Structure

```
resume-content-extractor/
├── server.py
├── extract_from_doc.py
├── extract_from_docx.py
├── extract_from_pdf.py
├── extract_email.py
├── extract_phoneno.py
├── extract_name.py
├── extract_edu.py
├── test.py
├── templates/
│   └── index.html
├── uploads/
├── data.csv
├── cert.pem
└── key.pem
```

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Access the application through your web browser:
   ```
   https://localhost:5000
   ```

3. Upload resume files through the web interface

4. Download the extracted data in CSV format using the download button

## API Endpoints

- `GET /`: Serves the main application page
- `POST /upload`: Handles file uploads and processes resumes
  - Accepts multiple files in the 'resumes' field
  - Returns JSON response indicating success/failure
- `GET /download`: Downloads the extracted data in CSV format

## Security Features

- HTTPS encryption using SSL certificates
- CORS (Cross-Origin Resource Sharing) support
- Upload directory validation
- File extension validation

## Output Format

The extracted data is saved in `data.csv` with the following columns:
- Name
- Email
- Phone No
- Education

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Troubleshooting

### Common Issues:

1. **SSL Certificate Error**:
   - Ensure `cert.pem` and `key.pem` are in the root directory
   - Generate new certificates if expired

2. **File Upload Issues**:
   - Check if the 'uploads' directory exists and has write permissions
   - Verify supported file formats (PDF, DOC, DOCX)

3. **Extraction Errors**:
   - Ensure all required Python packages are installed
   - Verify NLTK and spaCy data is downloaded


## Contact

For any questions or issues, please open an issue in the GitHub repository.
