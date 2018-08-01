# o arquivo server_side recebe connections do app dos celulares e salva os dados em um arquivo, 
# posteriormente se deve arquivar os dados em um banco de dados
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

import logging
from jsonrpc import JSONRPCResponseManager, dispatcher
import json
import simplejson as sjson
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
import logging
import config
import os

def dia_hora():
    return " -- "+time.strftime('%d/%m/%y %X')

logging.basicConfig(filename=os.path.join(config.path,'serrazul_app.log'),level=logging.DEBUG)
logging.info("o programa server_side.py foi iniciado"+dia_hora())
# registro de logs

#world = gpd.read_file('/home/daniel/workspaces/serrazul/geo/teste/stations3.geojson')
# carrega os dados, estes estao no formato geojson

@dispatcher.add_method
def atualiza_geojson_file(**kargs):
    global configg
    world = gpd.read_file(os.path.join(config.path,'stations3.geojson'))
    ext_data = kargs
    print kargs
    configg = kargs
    config_t = configg
    configg = json.dumps(configg)
    config_dict = sjson.loads(configg)
    print config_dict['lon']
    
    # A orde eh:
    # Point(longitude,latitude)
    data = {'name': ['pocos'],
            'marker-color': ['#0000ff'],
            'marker-symbol': ['zoo'],
            'line':['blue'],
            'geometry':[shapely.geometry.Point(config_dict['lon'],config_dict['lat'])]
            }


    f2 = pd.DataFrame(data)

    world = world.append(f2).reset_index(drop=True)
    with open(os.path.join(config.path,'stations3.geojson'), 'w') as ff:
        ff.write(world.to_json())

  
    return 'salvo'

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(config.url, int(config.porta_server_side), application)

 