from flask import render_template, request,jsonify
from app import app
import codecs
import re
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/')
def root():
	return render_template('main.html')

@app.route('/', methods=['GET','POST'])

def templetManager():
	if request.method == 'POST':
			
			f = request.files['file']
			
			if f:
				filename = secure_filename(f.filename)
				print(filename)
				f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
				f1=codecs.open('uploads/'+filename, 'r')
				a=f1.read()
				data=[a]
				print(data,"===============")
				f.close()

				f1=open("template/showOutput.html","w")
				f1.write(a)
				f.close() 
				
				
				return render_template('codeFetch.html',data=data)

			return render_template('main.html',"file not uploads")
	

			
		
		
		

