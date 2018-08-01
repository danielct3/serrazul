# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 01:09:47 2018

@author: daniel
"""

import fiona; fiona.supported_drivers
import geojson
from geojson import Feature, Point
import geopandas as gpd
import shapely.geometry
from multiprocessing import Process

import time
import pandas as pd

import io
import zipfile
import requests
import json


world = gpd.read_file('/home/daniel/workspaces/serrazul/geo/version_2/stations5.geojson')
  
   
data = {'name': ['pocos'],
            'marker-color': ['#0000ff'],
            'marker-symbol': ['zoo'],
            'line':['blue'],
            'geometry':[shapely.geometry.Point(34,33)],
            'id':[''],
            
            }


f2 = pd.DataFrame(data)
#world = world.drop(world.index[[0]])
world = world.append(f2).reset_index(drop=True)
#world = world.append(f2).reset_index(drop=False)
#world = world.drop(world.index[[0]])
#df.drop(df.index[[1,3]])


with open('/home/daniel/workspaces/serrazul/geo/version_2/stations6.geojson', 'w') as ff:
    ff.write(world.to_json())
    
    
    
# No fim, acho que o melhor caminho é o de usar as características do gdp mesmo, e apenas incluir mais pontos    