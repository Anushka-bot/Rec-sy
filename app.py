from flask import Flask, flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os
import urllib.request
import face_rec as fr
import wikipedia

app = Flask(__name__)              # making an object of flask and passing the name

UPLOAD_FOLDER = 'static/'

ALLOWED_EXTENSIONS = {'jpg','png','ico','jpeg','heic','webp'}

app.secret_key = "cairocoders-ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/output', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath= "static/"+filename
            name = fr.classify_face(filepath)
            try:
                otput = wikipedia.summary(name, sentences = 30, auto_suggest=False, redirect=True)   #summary of the person from wikipidea
            except wikipedia.exceptions.DisambiguationError:
                return render_template('output.html', output_name=name)
            else:
                return render_template('output.html', output_name=name, wiki=otput)
    return redirect(request.url)
    
if __name__ == "__main__":
    app.run(debug=True)
