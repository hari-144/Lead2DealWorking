from flask import Flask, json, request, redirect, url_for, render_template, jsonify
from waitress import serve
from modules.utils import FileOperations, SplitPages
app = Flask(__name__, static_folder="static", template_folder="templates")

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

app.config.update(SECRET_KEY = b"Lead2Deal@2021")

files = FileOperations()
pdf = SplitPages()

@app.after_request
def add_header(response):
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max_age=0, no-cache, no-store, mist-revalidate, post-check=0, pre-check=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response






@app.route("/")
def index():
    result = files.__get_files__("processed_files")
    return render_template("index.html", context=result)

@app.post("/process_pdf")
def process_pdf():
    data = request.get_json()
    del_status = files.__delete_all__("static/processed_images")
    status, pages, file_details = pdf.__convert_page_to_image__(f"processed_files/{data['file_name']}", r"C:\users\Poppler\poppler-0.68.0_x86\poppler-0.68.0\bin")
    
    return file_details
# app.debug = True




# app.run(debug=True, port=9090)
serve(app,port=9090,threads=100, ipv6=True)


