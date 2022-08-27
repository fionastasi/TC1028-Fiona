import fastf1 as f1fast #Importar los datos y la telemetría de la F1
from fastf1 import plotting #Para hacer las gráficas
from matplotlib import pyplot as plt #Para hacer las gráficas


quali = f1fast.get_session(2022, 'Jeddah Corniche', 'Qualifying') #Importamos los datos de la quali de Jeddah
vueltas_quali = quali.load_laps(with_telemetry=True) #Importamos la telemetría de la quali

vuelta_rapida = vueltas_quali.pick_fastest() #Buscamos la vuelta más rápida de la Q3 (la ganadora de la pole) y sus datos
print("Pole position: Checo Perez")
print('Vuelta más rápida Q3: ',vuelta_rapida['LapTime']) #Obtiene el tiempo de la vuelta rápida
print('Neumático: ',vuelta_rapida['Compound']) #Obtiene el tipo de neumaticos usados en la vuelta rápida
print('Piloto: ',vuelta_rapida['Driver']) #Obtiene el nombre del corredor de la vuelta rápida
print('Equipo: ',vuelta_rapida['Team']) #Obtiene el nombre del equipo del corredor ganador de la pole