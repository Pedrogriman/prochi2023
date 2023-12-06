# correlacion.py
import numpy as np

def calcular_correlacion_por_comuna(datos_comuna, predictores):
    # Extract predictor variables and target variable
    X_comuna = datos_comuna[predictores]

    # Calculate correlation matrix
    corr_matrix = X_comuna.corr(method='pearson')

    # Prepare data for visualization
    tril = np.tril(np.ones(corr_matrix.shape)).astype(bool)
    corr_matrix[tril] = np.nan
    corr_matrix_tidy = corr_matrix.stack().reset_index(name='r')
    corr_matrix_tidy = corr_matrix_tidy.rename(columns={'level_0': 'variable_1', 'level_1': 'variable_2'})
    corr_matrix_tidy = corr_matrix_tidy.dropna()
    corr_matrix_tidy['r_abs'] = corr_matrix_tidy['r'].abs()
    corr_matrix_tidy = corr_matrix_tidy.sort_values('r_abs', ascending=False).reset_index(drop=True)

    return corr_matrix_tidy
    pass
