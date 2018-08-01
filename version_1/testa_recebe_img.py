# -*- coding: utf-8 -*-
"""
Created on Sun May 27 08:00:13 2018

@author: daniel
"""

import cStringIO
from werkzeug.datastructures import FileStorage,Headers, MultiDict
from werkzeug.wrappers import Request, Response
from werkzeug.utils import secure_filename
import os
from flask import Flask, request, redirect, url_for,flash,send_from_directory

UPLOAD_FOLDER = '/home/daniel/workspaces/serrazul/geo/version_1'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        f = request.files['image']
        print (request.__contains__)
        # if user does not select file, browser also
        # submit a empty part without filename
        #if file.filename == '':
        #    flash('No selected file')
        #    return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join('/home/daniel/workspaces/serrazul/geo/version_1',filename))
            return redirect(url_for('uploaded_file',filename=filename))
            #return "a imagem foi salva"                        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 6003))
    app.run(host='0.0.0.0', port=port,debug=True)    

'''
decoded_data = Request.json['entry']['screenshots'].decode('base64')
file_data = cStringIO.StringIO(decoded_data)
file = FileStorage(file_data, filename='screenshot.jpg', mimetype='application/json')

if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save('/home/daniel/workspaces/serrazul/geo/version_1/teste.jpeg', filename))
    return redirect(url_for('uploaded_file',filename=filename))
    
'''    
    