'''
Proyecto de telemetría
'''

#bibliotecas:
import pandas as pd
from timple.timedelta import strftimedelta
import fastf1.plotting
from fastf1.core import Laps
import fastf1 as f1fast #Importar los datos y la telemetría de la F1
from fastf1 import plotting #Para hacer las gráficas
from matplotlib import pyplot as plt #Para hacer las gráficas
import statistics

def menuInicial():
    print("Bienvenido!")
    print("Resultados Quali = 1")
    print("Comparar al ganador de la Pole con cualquier corredor del TOP 5 = 2")
    print("Salir = 3")

def menu2():
    print("1.-LEC")
    print("2.-SAI")
    print("3.-VER")
    print("4.-OCO")
    
def main():
    quali = f1fast.get_session(2022, 'Jeddah Corniche', 'Qualifying')
    vueltas_quali = quali.load_laps(with_telemetry=True)
    menuInicial()
    print("Elige el número de la opción deseada:")
    opcion=int(input())
    while True:
        if opcion == 1: #definir opcion
            session = fastf1.get_session(2022, 'Jeddah Corniche', 'Qualifying')
            session.load()
            drivers = pd.unique(session.laps['Driver'])
            print(drivers)
            list_fastest_laps = list()
            for drv in drivers:
                drvs_fastest_lap = session.laps.pick_driver(drv).pick_fastest()
                list_fastest_laps.append(drvs_fastest_lap)
            fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)
            pole_lap = fastest_laps.pick_fastest()
            fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']
            print(fastest_laps[['Driver', 'LapTime', 'LapTimeDelta']])
        elif opcion==2:
            menu2()
            print("Elija a un corredor del Top 5 para ser comparado con el ganador de la Pole (número de la opción deseada):")
            opcion2 = int(input())
            while True:
                if opcion2 == 1:
                    fig, ax = plt.subplots(figsize=(15,8))
                    for driver in ['PER', 'LEC']:
                        lap = vueltas_quali.pick_driver(driver).pick_fastest()
                        tel = lap.get_telemetry()
                        ax.plot(tel['Distance'], tel['Speed'], label=driver)
                    ax.set_xlabel('Distancia (m)')
                    ax.set_ylabel('Velocidad (km/h)')
                    ax.set_title('Última vuelta Q3 (Checo vs Leclerc)')
                    ax.legend()
                    plt.show()
                print("Selecciona otra opción")
                menuInicial()
                opcion=int(input())
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
                print("Selecciona otra opción")
                menuInicial()
                opcion=int(input())
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
                print("Selecciona otra opción")
                menuInicial()
                opcion=int(input())
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
                print("Selecciona otra opción")
                menuInicial()
                opcion=int(input())
        elif opcion == 3:
            print("Gracias por su visita!")
            break
        else:
            print("Selecciona otra opción")
        menuInicial()
        opcion=int(input())

main()
            
                    
                        
                        
                            
                            
                            
                            
                        
                        
              