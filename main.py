#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from pprint import pprint

from flight_data import *
from flight_search import FlightSearch


#TODO:VAMOS A CHEQUIAR SI NUESTRA BASE DE DATOS　"GOOGLE SHEET" TIENE EN LA COLUMNA "IATACODE" DATOS GUARDADOS
        
        
#creamos obteto de nuestra nueva clase, que administra el google sheet
datamanager=DataManager()


#llamamos almetodo 'get_method' guardamos los datos obtenidos con get requests en una variable
sheet_data=datamanager.get_method()['prices']
pprint(f'probando sheet data  ')
pprint(sheet_data)
print()


#sheet data es una lista de diccionarios
for item in sheet_data:
    
    #si el　valor relacionado con la clave 'iatacode' esta vacio, agregamos el codigo IATA a la clave 'iatacode'
    if item['iataCode']=='':
        
        #creando objeto de la clase FlightData, que devolvera el  codigo IATA code de las ciudades
        flight_data=FlightData()
        
        
        #metodo de nuestra clase que se encagar de buscar el codigo de la ciudad, le pasamos toda informacion en sheet data
        #y el metodo se encargara de procesar la informacion
        iata_code_data=flight_data.get_destination_code(sheet_data)


        print('imprimiendo iata_code_data')
        print(iata_code_data)
        
        
        #NOTE: iata_code es una lista de codigos de ciudad, ver flight_data.py
        
        
        #aptualizamos los datos guardados en 'json_response' con el  metodo 'update_iata_code' de la clase DataManager()
        datamanager.update_iata_code(iata_code_data)
        
        
        #meotod que envia los datos guardados en 'json_response' al google docs
        datamanager.put_method()
        
        


        
    #para que no se esta repitiendo el proceso una y otra vez para cada item en el sheetdata, es decir en el google docs    
    break    

i=0 

#creando objeto de la clase FlightData, que devolvera el  codigo IATA code de las ciudades
flight_data=FlightData()


#incrustando las ciudades (codigo IATA de la city) en la clase FlightSearch, que se encarga de buscar la info de los vuelos
flight_search=FlightSearch()

    

#metodo de nuestra clase que se encagar de buscar el codigo de la ciudad, le pasamos toda informacion en sheet data
#y el metodo se encargara de procesar la informacion
iata_code_data=flight_data.get_destination_code(sheet_data)


#esta clase se encarga de la estrucutra para mandar los msj al celular 
notification_manager = NotificationManager()


#sheet data es una lista de diccionarios
for row in sheet_data:


    flight=flight_search.check_flights(search_city=iata_code_data[i] )

   
    #comparando el precio minimo definido en el google docs con el preci que nos de vuelve nuestra api
    if flight['price'] < row['lowestPrice']:
        
        print('probando, yes el valor es menor para bogota')
    
        notification_manager.send_sms(message=f"Low price alert! Only £{flight['price'] } to fly from {flight['origin_city'] }-{flight['origin_airport']} to {flight['destination_city']}-{flight['destination_airport']}, from {flight['out_date']}")

    i=i+1 
    
