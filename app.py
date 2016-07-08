from flask import Flask, render_template, redirect, request
import pdfkit
import os
from PyPDF2 import PdfFileReader, PdfFileMerger


app = Flask(__name__)


@app.route('/')
def select_scanner():
    return render_template('index.html')


@app.route('/pdf', methods=['POST'])
def to_pdf():
    html = request.form.get('hidden_element')
    #with open('C:\\Users\\gpatil\\Desktop\\HTML_to_PDF_Merge\\templates\\index.html') as f:
        #pdfkit.from_file(f, 'make1.pdf')
    file_path = os.path.join(os.getcwd(), "sample4.pdf")
    options = {
        'dpi': '600'
    }
    pdfkit.from_string(html, file_path, options=options)
    list_paths = [file_path, "C:\Users\gpatil\Desktop\New\sample1.bmp",
                  "C:\Users\gpatil\Desktop\New\sample2.pdf"]


    files_dir = "C:\Users\gpatil\Desktop\HTML_to_PDF_Merge"
    pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
    merger = PdfFileMerger()

    for filename in pdf_files:
        merger.append(PdfFileReader(os.path.join(files_dir, filename), True))

    merger.write(os.path.join(files_dir, "merged_full.pdf"))
    return "Done"


if __name__ == "__main__":
    app.run(debug=True)

