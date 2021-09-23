
from flask import Flask, render_template, Response, jsonify,request
import os
from os import path
from pathlib import Path
import testing_caption_generator as tcg


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html",template_folder='templates')


@app.route('/result',methods=['GET'])
def imageUpload():
    imgPath=''
    res=tcg.result(imgPath)
    return res




if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")