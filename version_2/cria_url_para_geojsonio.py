# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:28:30 2018

@author: daniel
"""
import geojsonio

from geojsonio import display

with open('/home/daniel/workspaces/serrazul/geo/version_2/stations6.geojson') as f:
    contents = f.read()
    #print geojsonio.make_url(contents)
    #print contents
    display(contents)
    print geojsonio.make_url(contents)
    