from pprint import pprint
import requests

from constants import *


class DataManager():
#     # Esta clase es responsable de interactuar con Google Sheet.
#     #TODO: ESCRIBIR Y ENVIAR DATA AL GOOGLE SHEET QUE ES NUESTRO 'DATABASE'
   
    def __init__(self):
                    
        # API　que usaremos para enviar y recibir informacion a nuestro google sheet
        self.url = SHEETY_API
        
    
    #meotod get() que utiliza  la API para obtener informacion del google sheet o base de datos   
    def get_method(self):
        
        #get request 
        response=requests.get(url=self.url)
        
        
        #imprime una respuesta http
        pprint(response.status_code)
        
        
        #leemos los datos en formato json
        self.json_response=response.json()
        
        
        #imprimimos la informacion  obtenida la google sheet
        pprint('Information obtained from the Google Sheet with the get method ')
        print(self.json_response)
        print()
        
        
        #retornamos los datos obtenidos del metodo get()
        return self.json_response
        
    
    #actualizando el valor de la columna IATA Code en nuestra google sheet
    def update_iata_code(self, iata_code_data):
        
        i=0 #iata_code_data es una lista, por lo tanto debemos recorrer, cada elemento de nuestra lista empezando por la posicion '0'
        
        
        #ciclo for que recorre nuestros datos guardados en json_response, en la clave 'prices'
        for item in self.json_response['prices']:
            
            #guardamos nuevo valor en la clave  'IATA code', columna de nuestro google sheet
            item['iataCode']=iata_code_data[i]

            i=i+1
           
        print()
        print('imprimiendo el nuevo json response con los datos "IATA code" actualizados')
        pprint(self.json_response)
        print()
        
        
    #Metodo put para enviar y almacenar informacion　en nuestra base de datos 'google sheet'
    def put_method(self):
        
        #ciclo for que recorre nuestros datos guardados en json_response, en la clave 'prices', que ya estan acualizados
        for i in range(2, len(self.json_response['prices'])+2):#en nuestro google sheet los datos empiezan desde la fila "2"
            
            
            #nuestra url + el [objeto id] que viene siendo el numero de la fila, mirar api documentation para mas informacion
            new_url= f'{self.url}/{i}'
            
            
            #NOTE: la sheety api, exige que los datos a enviar esten en formato json, guardados en un clave 'price', no 'prices'
            
            
            # #datos que se desean actualizar para 1 sola fila, los datos se actualizan fila por fila, cada diccionario representa 1 fila
            data={'price':self.json_response['prices'][i-2]}#[i-2] representa nuestro diccionario en la posicion 0
            
            
            #enviamos el request con el metodo put
            responde=requests.put(url=new_url , json=data)

            
            pprint(responde)
            print()
            
            pprint(responde.content)    
            print()
        
        
