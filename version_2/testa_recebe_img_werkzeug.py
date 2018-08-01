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
import requests

UPLOAD_FOLDER = '/home/daniel/workspaces/serrazul/geo/version_1'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



decoded_data = request.json['entry']['screenshots'].decode('base64')
file_data = cStringIO.StringIO(decoded_data)
f = FileStorage(file_data, filename='screenshot.jpg', mimetype='application/json')

if f and allowed_file(f.filename):
    filename = secure_filename(f.filename)
    f.save(os.path.join('/home/daniel/workspaces/serrazul/geo/version_1',filename))
    #return redirect(url_for('uploaded_file',filename=filename))
    
    
if __name__ == '__main__':    
    run_simple('localhost',6003,application,use_debuger=True,use_reloader=True)   