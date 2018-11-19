from flask import Flask
from werkzeug.utils import secure_filename
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
         return render_template('index.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post %d' % post_id

@app.route('/C_2/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/1/',methods=['GET','POST'])
def upload_file():
    if request.method =='POST':
        f = request.files['file']
        f.save('./C_2/'+secure_filename(f.filename))
        return render_template('ok.html')
    return render_template('NO.html')
