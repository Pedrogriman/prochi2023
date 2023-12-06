# predicciones_graficas.py
import pandas as pd

def procesar_datos(perico, all_predictions_by_comuna, metros_cuadrados_criterio, dormitorios_criterio, banos_criterio):
    # Obtener datos originales
    datos_originales = perico[['ID','Comuna', 'Barrio', 'Vendedor', 'MetrosC', 'Dormitorios', 'Baños','Aire acondicionado', 'Ascensor', 'Calefacción', 'Con área verde', 'Estacionamientos', 'Admite mascotas']]

    # Mapear datos originales
    mapeo = {0: 'No', 1: 'No', 2: 'Sí'}
    columnas_a_cambiar = ['Aire acondicionado', 'Ascensor', 'Calefacción', 'Con área verde', 'Estacionamientos', 'Admite mascotas']
    datos_originales.loc[:, columnas_a_cambiar] = datos_originales.loc[:, columnas_a_cambiar].replace(mapeo)

    # Cruce de datos originales con predicciones por comuna
    datos_con_predicciones = pd.merge(datos_originales, all_predictions_by_comuna, left_on='Comuna', right_on='Comuna', how='left')

    # Filtrar las mejores predicciones
    mejores_predicciones = datos_con_predicciones.dropna(subset=['Predictions'])

    # Filtrar opciones disponibles sin duplicados
    opciones_disponibles_sin_duplicados = mejores_predicciones[
        mejores_predicciones['MetrosC'].between(metros_cuadrados_criterio - 2, metros_cuadrados_criterio + 2) &
        mejores_predicciones['Dormitorios'].between(dormitorios_criterio - 0.01, dormitorios_criterio + 0.01) &
        mejores_predicciones['Baños'].between(banos_criterio - 0.01, banos_criterio + 0.01)
    ]

    # Eliminar duplicados basados en ciertas columnas
    opciones_disponibles_sin_duplicados = opciones_disponibles_sin_duplicados.drop_duplicates(
        subset=['Comuna', 'Barrio', 'Vendedor', 'MetrosC', 'Dormitorios', 'Baños']
    )

    return opciones_disponibles_sin_duplicados
    pass
