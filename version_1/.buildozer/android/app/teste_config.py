# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:52:48 2018

@author: daniel
"""
import os
import config
print config.truck['color']  
print config.url


print config.path

print type(os.path.join(config.path,'stations3.geojson'))
print os.path.join(config.path,'stations3.geojson')