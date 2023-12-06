# mapeo_datos.py
import pandas as pd

def mapear_valores(datos):
    mapeo = {0: 0, 1: 0, 2: 1}
    columnas_a_cambiar = ['Condicion', 'Acceso a internet', 'Aire acondicionado', 'Ascensor', 'Calefacción', 'Con área verde', 'Estacionamientos', 
                         'Gas natural', 'TV por cable', 'Admite mascotas', 'Agua corriente', 'Rampa para silla de ruedas', 'Conserjería', 'Seguridad']
    datos.loc[:, columnas_a_cambiar] = datos.loc[:, columnas_a_cambiar].replace(mapeo)

    return datos
