# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:53:15 2018

@author: daniel

Arquivo de configuração para todo o sistema do aplicativo serrazul versão 

"""
import os

# url do servidor
url = '0.0.0.0'

# porta do server_side 
porta_server_side = '6000'

# path dir - diretório onde está instalado o programa
c_path = '/home/daniel/workspaces/serrazul/geo/version_1/'
path = os.path.abspath(c_path)

truck = dict(
    color = 'blue',
    brand = 'ford',
)
city = 'new york'
cabriolet = dict(
    color = 'black',
    engine = dict(
        cylinders = 8,
        placement = 'mid',
    ),
    doors = 2,
)