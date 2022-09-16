from fastapi import FastAPI
import json

app = FastAPI() #Asignamos FastApi a 


@app.get("/")
async def root():
    return {'bienvenido': 'Bienvenido a la evaluacion sobre API REST'}

circuits_open = open('../PI01_DATA02/Datasets/circuits.json', 'r') #Abrimos nuestro Json

circuits_read = circuits_open.read() #Leemos nuestro Json

circuits = json.loads(circuits_read) #Cargamos nuestro Json en una variable

@app.get("/circuits") #Hacemos un get sobre el servidor
async def root_circuits():
    return circuits

lap_times_total_open = open('../PI01_DATA02/Datasets/lap_times_total.json', 'r') #Abrimos nuestro Json

lap_times_total_read = lap_times_total_open.read() #Leemos nuestro Json

lap_times_total = json.loads(lap_times_total_read) #Cargamos nuestro Json en una variable

@app.get("/lap_times_total") #Hacemos un get sobre el servidor
async def root_lap_times_total():
    return lap_times_total

pit_stops_open = open('../PI01_DATA02/Datasets/pit_stops.json', 'r') #Abrimos nuestro Json

pit_stops_read = pit_stops_open.read() #Leemos nuestro Json

pit_stops = json.loads(pit_stops_read) #Cargamos nuestro Json en una variable

@app.get("/pit_stops") #Hacemos un get sobre el servidor
async def root_pit_stops():
    return pit_stops


qualifying_total_open = open('../PI01_DATA02/Datasets/qualifying_total.json', 'r') #Abrimos nuestro Json

qualifying_total_read = qualifying_total_open.read() #Leemos nuestro Json

qualifying_total = json.loads(qualifying_total_read) #Cargamos nuestro Json en una variable

@app.get("/qualifying_total") #Hacemos un get sobre el servidor
async def root_qualifying_total():
    return qualifying_total


races_open = open('../PI01_DATA02/Datasets/races.json', 'r') #Abrimos nuestro Json

races_read = races_open.read() #Leemos nuestro Json

races = json.loads(races_read) #Cargamos nuestro Json en una variable

@app.get("/races") #Hacemos un get sobre el servidor
async def root_races():
    return races

results_open = open('../PI01_DATA02/Datasets/results.json', 'r', encoding='utf8') #Abrimos nuestro Json

results_read = results_open.read() #Leemos nuestro Json

results = json.loads(json.dumps(results_read)) #Este tipo de Json tiene un coportamiento diferente, el interprete identifica esto como un conjunto de diccionarios, por lo que se aplica el metodo DUMPS

@app.get("/results") #Hacemos un get sobre el servidor
async def root_results():
    return results


constructors_open = open('../PI01_DATA02/Datasets/constructors.json', 'r', encoding='utf8') #Abrimos nuestro Json

constructors_read = constructors_open.read() #Leemos nuestro Json

constructors = json.loads(json.dumps(constructors_read)) #Este tipo de Json tiene un coportamiento diferente, el interprete identifica esto como un conjunto de diccionarios, por lo que se aplica el metodo DUMPS

@app.get("/constructors") #Hacemos un get sobre el servidor
async def root_constructors():
    return constructors


drivers_open = open('../PI01_DATA02/Datasets/drivers.json', 'r', encoding='utf8') #Abrimos nuestro Json

drivers_read = drivers_open.read() #Leemos nuestro Json

drivers = json.loads(json.dumps(drivers_read)) #Este tipo de Json tiene un coportamiento diferente, el interprete identifica esto como un conjunto de diccionarios, por lo que se aplica el metodo DUMPS

@app.get("/drivers") #Hacemos un get sobre el servidor
async def root_drivers():
    return drivers
