'''
Proyecto de telemetría
El programa desplegará un menú relacionado con los resultados de la Quali de Jeddah Corniche del 2022
Al final imprime y grafica resultados
'''

#importar las bibliotecas:
import pandas as pd
from timple.timedelta import strftimedelta
import fastf1.plotting
from fastf1.core import Laps #Importar las vueltas 
import fastf1 as f1fast #Importar los datos y la telemetría de la F1
from fastf1 import plotting #Para hacer las gráficas
from matplotlib import pyplot as plt #Para hacer las gráficas

def menuInicial(): #Menú incial que se desplegará al principio
    print("Bienvenido!")
    print("Resultados Quali = 1")
    print("Comparar al ganador de la Pole con cualquier corredor del TOP 5 = 2")
    print("Salir = 3")

def menu2(): #Desplegará el segundo menú con los corredores al elegir la opción 2 en el menú principal
    M=[
       ['PER, vs, LEC(1)'],
       ['PER, vs, SAI(2)'],
       ['PER, vs, VER(3)'],
       ['PER, vs, OCO(4)'],
      ]
    print(M)
def main():
    quali = f1fast.get_session(2022, 'Jeddah Corniche', 'Qualifying') #Obtener los datos de la Quli
    vueltas_quali = quali.load_laps(with_telemetry=True) #Importar la telemetría de la quali
    menuInicial() #Llamar el menú inicial
    print("Elige el número de la opción deseada:")
    opcion=int(input()) #Input para elegir la opción del menú inicial
    while True:
        if opcion == 1: #definir opcion, e importar los resultados de la quali y desplegarlo como lista
            session = fastf1.get_session(2022, 'Jeddah Corniche', 'Qualifying')#Obtener los datos de la Quli
            session.load()
            drivers = pd.unique(session.laps['Driver'])#Cargar a los corredores
            print(drivers)
            list_fastest_laps = list() #Imprimirlos y listarlos 
            for drv in drivers:
                drvs_fastest_lap = session.laps.pick_driver(drv).pick_fastest()
                list_fastest_laps.append(drvs_fastest_lap)
            fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)
            pole_lap = fastest_laps.pick_fastest()
            fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']
            print(fastest_laps[['Driver', 'LapTime', 'LapTimeDelta']])#Imprime los resultados de la última vuelta de la Quali
        elif opcion==2: #en caso de la opción 2 desplegará el menú 2 y podrás elegir a un corredor a comparar con Checo
            menu2()
            print("Elija a un corredor del Top 5 para ser comparado con el ganador de la Pole (número de la opción deseada):")
            opcion2 = int(input())
            while True:
                if opcion2 == 1: #Este código se repite en todas las opciones, es para obtener los datos de los corredores
                    #y hacer una gráfica para compararlos
                    fig, ax = plt.subplots(figsize=(15,8))
                    for driver in ['PER', 'LEC']:#Definir al corredor con el que Checo será comparado 
                        lap = vueltas_quali.pick_driver(driver).pick_fastest()
                        tel = lap.get_telemetry()#Obtener la telemtría de la última vuelta de los dos corredores
                        ax.plot(tel['Distance'], tel['Speed'], label=driver)#Las líneas 62-67 son para el formato de la gráfica
                    ax.set_xlabel('Distancia (m)')
                    ax.set_ylabel('Velocidad (km/h)')
                    ax.set_title('Última vuelta Q3 (Checo vs Leclerc)')
                    ax.legend()
                    plt.show()
                if opcion2 == 2:
                    fig, ax = plt.subplots(figsize=(15,8))
                    for driver in ['PER', 'SAI']:
                        lap = vueltas_quali.pick_driver(driver).pick_fastest()
                        tel = lap.get_telemetry()
                        ax.plot(tel['Distance'], tel['Speed'], label=driver)
                    ax.set_xlabel('Distancia (m)')
                    ax.set_ylabel('Velocidad (km/h)')
                    ax.set_title('Última vuelta Q3 (Checo vs Sainz)')
                    ax.legend()
                    plt.show()
                if opcion2 == 3:
                    fig, ax = plt.subplots(figsize=(15,8))
                    for driver in ['PER', 'VER']:
                        lap = vueltas_quali.pick_driver(driver).pick_fastest()
                        tel = lap.get_telemetry()
                        ax.plot(tel['Distance'], tel['Speed'], label=driver)
                    ax.set_xlabel('Distancia (m)')
                    ax.set_ylabel('Velocidad (km/h)')
                    ax.set_title('Última vuelta Q3 (Checo vs Verstappen)')
                    ax.legend()
                    plt.show()
                if opcion2 == 4:
                    pilotos= ['PER', 'OCO']
                    fig, ax = plt.subplots(figsize=(15,8))
                    for driver in pilotos:
                        lap = vueltas_quali.pick_driver(driver).pick_fastest()
                        tel = lap.get_telemetry()
                        ax.plot(tel['Distance'], tel['Speed'], label=driver)
                    ax.set_xlabel('Distancia (m)')
                    ax.set_ylabel('Velocidad (km/h)')
                    ax.set_title('Última vuelta Q3 (Checo vs Ocon)')
                    ax.legend()
                    plt.show()
        elif opcion == 3: #Con esta opción se sale del código y se rompe el ciclo
            print("Gracias por su visita!")
            break
        else: #En caso de elegir una opción inexistente, te pide otra vez seleccionar una opción.
            print("Selecciona otra opción")
        menuInicial()
        opcion=int(input())

main()              