
from flask import Flask, render_template, request, jsonify, Response
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import requests
import os
import json
import base64 

from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
     file = FileField("File", validators=[InputRequired()])
     submit = SubmitField("Upload File")

im_data = {}     
convID = 0
@app.route('/get_ID', methods=['POST'])
def get_ID():
  req_data = json.loads(request.data, strict=False)
  convID = req_data["convID"]
  im_data[convID] = ''




@app.route('/', methods = ['GET', 'POST'])
def hello_world():
        form = UploadFileForm()
        if form.validate_on_submit():
             file = form.file.data
             file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
             with open(r"C:\\Users\\Fanny\\OneDrive\\Desktop\\ml\\vscode projects\\airecom\\static\\files\\wallpaper.jpeg", "rb") as imageFile:
                 str = base64.b64encode(imageFile.read())
             im_data[convID] = "Hello"
             r= requests.get("http://52.56.126.51/")
             print(im_data)
             #r = requests.post("http://52.56.126.51/img_upload", data = json.dumps(im_data))
             print(r.text)
             return "File has been successfully uploaded"
        
        return render_template("img.html", form = form)

if __name__ == "__main__":
  app.run(debug=True)