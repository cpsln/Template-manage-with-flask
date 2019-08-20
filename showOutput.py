from flask import render_template, request,jsonify
from app import app
import codecs
import re
	
@app.route('/newData')
def root1():
    return render_template('showOutput.html')
    