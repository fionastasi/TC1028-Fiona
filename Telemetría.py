import fastf1 as f1fast #Importar los datos y la telemetría de la F1
from fastf1 import plotting #Para hacer las gráficas
from matplotlib import pyplot as plt #Para hacer las gráficas

plotting.setup_mpl()


quali = f1fast.get_session(2022, 'Jeddah Corniche', 'Qualifying') #Importamos los datos de la quali de Jeddah
vueltas_quali = quali.load_laps(with_telemetry=True) #Importamos la telemetría de la quali

vuelta_rapida = vueltas_quali.pick_fastest() #Buscamos la vuelta más rápida de la Q3 (la ganadora de la pole) y sus datos
print("Pole position: Checo Perez")
print('Vuelta más rápida Q3: ',vuelta_rapida['LapTime']) #Obtiene el tiempo de la vuelta rápida
print('Neumático: ',vuelta_rapida['Compound']) #Obtiene el tipo de neumaticos usados en la vuelta rápida
print('Piloto: ',vuelta_rapida['Driver']) #Obtiene el nombre del corredor de la vuelta rápida
print('Equipo: ',vuelta_rapida['Team']) #Obtiene el nombre del equipo del corredor ganador de la pole

fig, ax = plt.subplots(figsize=(15,8)) #Definimos el tamaño de la gráfica que vamos a crear
for driver in ['PER', 'LEC']: #Elegimos a nuestros pilotos a comparar
    lap = vueltas_quali.pick_driver(driver).pick_fastest() #La vuelta más rápida es de la cual obtenemos los datos
    tel = lap.get_telemetry() #Obtenemos la telemetría de la vuelta que queremos
    ax.plot(tel['Distance'], tel['Speed'], label=driver) #Con esto organizamos la gráfica con distancia y velocidad, así también se ponen las leyendas para saber los pilotos y sus resultados

ax.set_xlabel('Distancia (m)') #Establecemos que en el eje "x" va la distancia
ax.set_ylabel('Velocidad (km/h)') #Establecemos que en el eje "y" va la velocidad
ax.set_title('Última vuelta Q3 (Checo vs Leclerc)') #Establecemos el titulo pondremos
ax.legend() #Mostrámos la leyenda
plt.show() #Hacemos que al darle play al programa nos muestre la gráfica final