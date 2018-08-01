# -*- coding: utf-8 -*-
"""
Created on Sun May 27 06:10:35 2018

@author: daniel
"""

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.post("http://httpbin.org/post", data=payload)

# vou usar sempre 6003 para o novo servidor web que receberá a imagem
url = "http://192.168.0.110:6003"

#files = {'media': open('/home/daniel/Desktop/2.jpeg', 'rb')}
#requests.post(url,files=files)



with open('/home/daniel/Desktop/2.jpeg', 'rb') as f:
    requests.post(url, data={'location': 'teste', 'status': 'teste' }, files={'image': f})
