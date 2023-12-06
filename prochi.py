pip install seaborn
from librerias_datos import leer_datos, limpiar_datos
from mapeo_datos import mapear_valores
from correlacion import calcular_correlacion_por_comuna
from entrenamiento_resultados import train_model_and_evaluate
from prediccion_comuna import calculate_predictions_by_comuna
from diagnostico import plot_diagnostic_plots
from vif import calculate_vif
from predicciones_graficas import make_predictions_and_plot
from procesamiento_datos import procesar_datos

comunas_unicas = datos['Comuna'].unique()

predictions_by_comunas = pd.DataFrame()
all_predictions_by_comuna = pd.DataFrame()
for comuna in comunas_unicas:
    datos_comuna = datos[datos['Comuna'] == comuna]

    # Train the model and evaluate
    modelo_final, X_train_selected, residuos_comuna, y_train_comuna, result, X_train_comuna, features_excluding_comuna, sfs, X_test_comuna, y_test_comuna = train_model_and_evaluate(datos_comuna)

    # Plot diagnostic plots
    plot_diagnostic_plots(y_train_comuna[:result['len_train_comuna']], result['y_pred_train_comuna'], residuos_comuna, comuna)

    # Calculate VIF
    vif_by_comuna = calculate_vif(X_train_comuna, features_excluding_comuna, comuna)

    # Make predictions and plot
    predictions_by_comuna, predictions_by_comunas, error = calculate_predictions_by_comuna(comuna, modelo_final, sfs, X_test_comuna, features_excluding_comuna, y_test_comuna)
    all_predictions_by_comuna = pd.concat([all_predictions_by_comuna, predictions_by_comuna], ignore_index=True)
    # Guardar en Excel
    all_predictions_by_comuna.to_excel(r'C:\Users\pedro.griman\Desktop\Pro_Chi\.venv\data\pred.xlsx')



    # Print results
    print(f"Shapiro-Wilk: {comuna}, Test Shapiro-Wilk: estadístico = {result['shapiro_test']}")
    print('_________________________________________________________________________________________')
    print(f"D'Agostino's K-squared: {comuna}, Test D'Agostino's K-squared: estadístico = {result['k2']}, p-value = {result['p_value']}")
    print('_________________________________________________________________________________________')
    print(f"Breuschpagan: {comuna}, Estadístico= {result['lm']}, p-value = {result['lm_p_value']}")
    print('_________________________________________________________________________________________')
    print(f"fvalue: {comuna}, Estadístico= {result['fvalue']}, p-value = {result['f_p_value']}")
    print('_________________________________________________________________________________________')
    print(f"Correlación para la comuna {comuna}:\n{result['correlacion_comuna']}\n")
    print('_________________________________________________________________________________________')
    print(f"VIF para la comuna {comuna}:\n{vif_by_comuna}\n")
    print('_________________________________________________________________________________________')
    print(f'Error de RMSE para {comuna}: {error}')
    print('_________________________________________________________________________________________')
    print(f'Predicciones {comuna}: {predictions_by_comuna}')

metros_cuadrados_criterio = 60
dormitorios_criterio = 3
banos_criterio = 1
# Llamar a la función procesar_datos
opciones_disponibles_sin_duplicados = procesar_datos(perico, all_predictions_by_comuna, metros_cuadrados_criterio, dormitorios_criterio, banos_criterio)


