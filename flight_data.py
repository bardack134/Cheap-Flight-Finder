from pprint import pprint
from constants import *
import requests
# from data_manager import *#borrar

#NOTE:Para buscar vuelos necesitamos un código de la Asociación Internacional de Transporte Aéreo (IATA) . 
# Este código ayuda a identificar aeropuertos y áreas metropolitanas.

        
class FlightData:#ESTA CLASE ES RESPONSABLE DE ESTRUCTURAR LOS DATOS DEL VUELO.
    
#TODO: PASAR LOS NOMBRES DE LA CIUDADES EN EL GOOGLE SHEET A ESTA CLASE

    def __init__(self):
        
        #TODO: OBTÉN LOS CÓDIGOS IATA UTILIZANDO LA API DE KIWI PARTNERS
        self.url=f'{TEQUILA_ENDPOINT}/locations/query'
        self.api_key = TEQUILA_API_KEY
       
    
    # Definimos un método para obtener el código IATA para una ciudad dada
    def get_destination_code(self, sheet_data):
        
        response_list=[]#lista donde se guardaran todos los valores del response 
        
     
        #NOTE* la informacion en nuestro google sheet, esta guarda en la variable 'sheet_data' (ver main.py file)
        
        
        
        #parametros que recibe deacuwerdo a la documentacion
        parameters={
            
            #aca debemos incluir los nombres de las ciudades de nuestro documento en google docs
            'term':'Medellin',
            'location_types':'city',
        }
        
        
        #NOTE: mas informacion ver https://tequila.kiwi.com/portal/docs/tequila_api/locations_api, respecto a los parametros que recibe la api
        
        
        headers={ #apikey en headers, para ocultar nuestra informacion
            'apikey':self.api_key,
            
        }
        
        
        #get requests
        response = requests.get(url=self.url, headers=headers, params=parameters) 
        
        
        #si es correcta la peticion agregamos la respuesta a la lista
        if response.status_code == 200: 
            response_list.append(response.json())
        
            
            #imprimimos respuesta http
            pprint("response status code: ") 
            print(response.status_code)
            print()
            
            
            pprint("informacion entregada por la clase FlightData() obtenida de la API Tequila")
            pprint(response.json())
            print()

            
            #revisando la informacion en la respuesta response, encontramos que el codigo esta guardado en la clave 'code'
            code=response.json()['locations'][0]['code']
            print(code)
        # code='TESTING 2'
        
        
        # return code
    


# #borrar
# flight_data=FlightData()

# datamanager=DataManager()
# flight_data.get_destination_code(sheet_data=datamanager.get_method()['prices'])