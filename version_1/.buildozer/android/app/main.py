# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer import vibrator
from plyer import gps
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


import subprocess
import requests
import json

from kivy.logger import Logger

#Logger.info('title: This is a info message.')


global url
#global filename
#url = "http://mayagorda.ddns.net:6000/"

url = "http://192.168.0.107:6001"

#DATA_URI  = "http://192.168.0.110:6003"

class VibrationInterface(BoxLayout):
    '''Root Widget.'''
    # tentativva de colcar o configure para ligar o gps quando se inicio o app
    #gps.configure(on_location=VibrationInterface.envia_posicao)
    
    def current_location2(self):
        try:
            gps.configure(on_location=self.envia_posicao)

            gps.start()
            #gps.stop()
            #requests.post(DATA_URI, data={'location': self.on_location})
            #popup = Popup(title="sei lah",content=Label(text='teste')).open()
            #Clock.schedule_once(lambda d: popup.dismiss(), 3)
            #print str(self.on_location)
            #self.envia_posicao(self.on_location)
            
        except NotImplementedError:
            popup = Popup(title="GPS Error",
                          content=Label(text="GPS support is not active on your platform")
                          ).open()
            Clock.schedule_once(lambda d: popup.dismiss(), 3)
            
    def picture_taken(self, obj, filename):
        #global filename
        #filename = filename
        print 'Picture taken and saved to', filename
        self.current_location2()
        print 'apos chamar a current_location2()'
        #with open(filename, 'rb') as f:
        #    print 'enviando o arquivo ', filemane
        #    requests.post(DATA_URI,data={'location': 'teste', 'status': 'teste' }, files={'image': f})
        
        



    
    def envia_posicao(self,**kwargs):
        # função feita para envio dos dados de posição e user para o server_side que irá persistir as posições
        global url
        #global filename
        #print "teste"
        #last=subprocess.check_output("w",shell=True)
        #ls=Popup(title="LOGIN",content=Label(text="logged in \n" + last))
        #ls.open()
        
        headers = {'content-type': 'application/json'}        
        payload = {
        "method": "atualiza_geojson_file",
        #"params": {'motor': False},
        "params": kwargs,    
        "jsonrpc": "2.0",
        "id": 2,
        }
      
        headers = {'content-type': 'application/json'}

        #print "filename dentro da func envia_posição ",filename

        #popup = Popup(title="GPS Error",
        #                  content=Label(text=" Até antes do request a func envia_posicao funcionou")
        #                  ).open()        
        
        r = requests.post(url,json.dumps(payload),headers=headers).json()
        #with open(filename, 'rb') as f:
        #    r = requests.post(url,json.dumps(payload),headers=headers,files={'image': f}).json()
        #manda_dados = requests.post(url,json.dumps(payload),headers=headers).json()
        gps.stop()          
        popup = Popup(title="enviando imagem",
                          content=Label(text="enviando imagem")
                          ).open()
        #Clock.schedule_once(lambda d: popup.dismiss(), 3)
        #popup = Popup(title="GPS Error",
        #                  content=Label(text=" Até depois do request a func envia_posicao funcionou")
        #                  ).open()  

   
   
      
   
class VibrationApp(App):

    def build(self):
        return VibrationInterface()   
   
if __name__ == '__main__':
    VibrationApp().run()
