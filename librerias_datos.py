# librerias_datos.py
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.eval_measures import rmse
from typing import Union

# Lectura de datos
def leer_datos(ruta):
    return pd.read_excel(ruta)

# Limpieza de datos
def limpiar_datos(datos):
    datos.drop(['Unnamed: 0.3', 'Unnamed: 0.2',	'Unnamed: 0.1',	'Estatus',	'Unnamed: 0', 'Region',	'Barrio',	'Vendedor', 'Tipo', 'Moneda', 'Moneda Gastos',  
            'Ambientes', 'Amoblado', 'Antigüedad', 'Área de cine', 'Área de juegos infantiles', 'Azotea', 'Balcón', 'Baño de visitas', 'Bodegas', 'Business center', 
            'Caldera', 'Cancha de básquetbol', 'Cancha de paddle', 'Cancha de tenis', 'Canchas de usos múltiples', 'Cantidad de pisos', 'Cantidad máxima de habitantes', 
            'Chimenea', 'Cisterna', 'Closets', 'Cocina', 'Comedor', 'Con cancha de fútbol', 'Con conexión para lavarropas', 'Con energia solar', 'Con TV satelital', 
            'Departamentos por piso', 'Desayunador', 'Disponible desde', 'Dormitorio en suite', 'Dormitorio y baño de servicio', 'Estacionamiento de visitas', 'Gastos comunes', 
            'Generador eléctrico', 'Gimnasio', 'Homeoffice', 'Jardín', 'Lavandería', 'Línea telefónica', 'Living', 'Logia', 'Número de piso de la unidad', 'Número de torre', 
            'Orientación', 'Patio', 'Piscina', 'Playroom', 'Quincho', 'Recepción', 'Refrigerador', 'Salón de fiestas', 'Salón de usos múltiples', 'Sauna', 'Superficie de terraza',
            'Terraza', 'Tipo de departamento', 'Uso comercial', 'Walk-in clóset', 'Jacuzzi', 'Tipo de seguridad', 'Con condominio cerrado', 'Mercado'],axis=1, inplace=True)
    pass
