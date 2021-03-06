from flask import Flask, render_template, Response, jsonify,request
import testing_caption_generator as tcg
from werkzeug.utils import secure_filename


app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template("index.html",template_folder='templates')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        pic = request.files['pic']
        pic.save(pic.filename)
    if not pic:
        return 'No pic uploaded!', 400

    desc=tcg.result(pic)
    return desc


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")
