from datetime import datetime, timedelta
from pprint import pprint
import requests
from constants import *
from notification_manager import NotificationManager




class FlightSearch:
    #Esta clase es responsable de interactuar con la API de Búsqueda de Vuelos.”
    
    # TODO: BUSCAMOS NUESTROS VUELOS USANDO LOS CODIGOS DE LA CIUDAD 
    
    def __init__(self):
        

        self.url=f'{TEQUILA_ENDPOINT}/v2/search'
        self.api_key = TEQUILA_API_KEY      
        

    #funcion que buscara informacion acerca de los vuelos a cada una de nuestras ciudades en el google docs
    def check_flights(self, search_city):
        
        tomorrow = datetime.now() + timedelta(days=1)
        
        
        #buscaremos solo vuelos de ida
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


        #pasamos en el header nuestro apikey para ocultar la info
        headers = {"apikey": TEQUILA_API_KEY}
        
        
        #NOTE:informacion que recibe la api, deacuerdo a la documentacion 'https://tequila.kiwi.com/portal/docs/tequila_api/search_api'
        query = {
            
            "fly_from": MY_CITY,
            "fly_to": search_city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            #buscaremos solo vuelos de ida
            "date_to": six_month_from_today.strftime("%d/%m/%Y"),  
            # FROM API_DATA If you are searching for a one-way flight, omit 'return_to' and 'return_from' or 'nights_in_dst_from' and 
            # "nights_in_dst_from": 7,
            # "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 10,
            "curr": "JPY",
            
        }

        
        #solicitud get, recibiendo parametros, headers para obtener nuestra informacion
        response = requests.get(
            url=self.url,
            headers=headers,
            params=query,
        ) 
        
        
        # #si es correcta la peticion agregamos la respuesta a la lista
        # if response.status_code == 200: 
        
        
        #imprimimos respuesta http
        pprint("response status code: ") 
        print(response.status_code)
        print()
        
    
        # print(response.json())
        print()
        
        
        #mirando el json response nos damos cuenta que los datos estan guardados en la clave 'data'
        data = response.json()["data"][0]
        
        # pprint(data)
        
        # guardo los datos obtenidos de la api en un diccionario
        data_dict={
        'price':data["price"],
        'origin_city':data["route"][0]["cityFrom"],
        'origin_airport':data["route"][0]["flyFrom"],
        'destination_city':data['cityTo'],
        'destination_airport':data["route"][0]["flyTo"],
        'out_date':data["route"][0]["local_departure"].split("T")[0],
        # 'return_date':data["route"][1]["local_departure"].split("T")[0]
        }


        print()
        pprint(data_dict)
        print(f"the destination city is {data_dict['destination_city']} and the price is {data_dict['price']}")
        print()
        
        
        return data_dict