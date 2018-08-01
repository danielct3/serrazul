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
import json
import config
import sqlite3 as sql

path = config.c_path
UPLOAD_FOLDER = config.img_path

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
          
       
        lon = float(request.form.getlist('lon')[0])
        #lon = request.form.getlist('lon')[0]
 
        lat = float(request.form.getlist('lat')[0])
        #lat = request.form.getlist('lat')[0]

        #nome_img = float(request.form.getlist('nome_img')[2])
        nome_img = request.form.getlist('nome_img')[0]

        #user = float(request.form.getlist('id')[3])
        user = int(request.form.getlist('id')[0])

        #print '0 ',lon,'1 ',lat,'2 ',nome_img,'3 ',user        
        
        data_list = [lon,lat,nome_img,user]    
        
        try:
            
            with sql.connect(config.db_path) as con:
                cur = con.cursor()
                print 'conectou com o bd'
                cur.execute('INSERT INTO positions (longitude,latitude,nome_img,id) VALUES (?,?,?,?)', data_list)
                con.commit()
        except:
            #print 'deu erro'
            con.rollback()
             #con.rollback()
        
        
        f = request.files['image']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(UPLOAD_FOLDER,filename))
            return redirect(url_for('uploaded_file',filename=filename))
        
        print json.dumps(request.form.getlist('status'))
        item = request.form.getlist('status') 
        print item[0]
        print 'sem json', request.form['status']            
        
        
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        #f = request.files['image']
        #print request.args.get('data')
        #print request.form.get('data')
        #print json.dumps(request.form.getlist('status'))
        #item = request.form.getlist('status') 
        #print item[0]
        #print 'sem json', request.form['status']      
        #num = item[0].encode("utf-8")
        #num = float(num)
        #print num
        #print type(num)
        #decoded_value = item.decode('utf-8', 'ignore')
        #print decoded_value
        #print type(json.dumps(request.form.getlist('status')))
        #print float(json.dumps(request.form.getlist('status')))
        #r = request.form.getlist('data')[2].json()
        #data = request.data
        #dataDict = json.loads(data)
        #print data
        #print request.values['data'][2]
        # if user does not select file, browser also
        # submit a empty part without filename
        #if file.filename == '':
        #    flash('No selected file')
        #    return redirect(request.url)
                               
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
    port = int(os.environ.get('PORT', config.porta_server_side))
    app.run(host=config.url, port=port,debug=True)    

