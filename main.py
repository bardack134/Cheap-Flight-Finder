#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from pprint import pprint

from flight_data import FlightData


#TODO:VAMOS A CHEQUIAR SI NUESTRA BASE DE DATOS　"GOOGLE SHEET" TIENE EN LA COLUMNA "IATACODE" DATOS GUARDADOS
        
        
#creamos obteto de nuestra nueva clase
datamanager=DataManager()


#llamamos almetodo 'get_method' guardamos los datos obtenidos con get requests en una variable
sheet_data=datamanager.get_method()['prices']
pprint(f'proibando sheet data  {sheet_data}')
print()


for item in sheet_data:
    if item['iataCode']=='':
        
        #creando objeto de la clase FlightData, que devolvera el  codigo IATA code de las ciudades
        flight_data=FlightData()
        
        
        iata_code_data=flight_data.get_destination_code()
        
        
        #aptualizamos los datos guardados y almacenados en json_response con el nuevo metodo 'update_iata_code'
        datamanager.update_iata_code(iata_code_data)
        
        
        #metodo put, para enviar los datos actualizados a nuestro google sheet
        datamanager.put_method()