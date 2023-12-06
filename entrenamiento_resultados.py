# entrenamiento_resultados.py
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.tools.eval_measures import rmse

def train_model_and_evaluate(datos_comuna):
    result=[]
    # Separate predictor and target variables

    X_comuna = datos_comuna.drop(columns='Precio')
    y_comuna = datos_comuna['Precio']

    # Split data into training and testing sets

    X_train_comuna, X_test_comuna, y_train_comuna, y_test_comuna = train_test_split(
        X_comuna, y_comuna, train_size=0.8, random_state=1234, shuffle=True)

    # Identify predictor variables excluding the commune variable

    features_excluding_comuna = [col for col in X_train_comuna.columns if col != 'Comuna']

    # Separate X_train without the commune variable

    X_train_without_comuna = X_train_comuna[features_excluding_comuna]

    # Initialize sequential feature selector
    sfs = SequentialFeatureSelector(
        LinearRegression(),
        n_features_to_select='auto',
        direction='forward',
        scoring='r2',
        cv=5
    )

    # Fit the sequential feature selector

    sfs.fit(X_train_without_comuna, y_train_comuna)

    # Obtain selected features

    selected_features = sfs.get_feature_names_out().tolist()
    selected_features_with_comuna = selected_features + ['Comuna']

    # Select the training data with selected features

    X_train_selected = X_train_comuna[selected_features_with_comuna]

    # Train the final linear regression model

    modelo_final = LinearRegression()
    modelo_final.fit(sfs.transform(X_train_without_comuna), y_train_comuna)

    # Make predictions on the training data

    y_pred_train_comuna = modelo_final.predict(sfs.transform(X_train_without_comuna))

    # Calculate residuals

    residuos_comuna = y_train_comuna - y_pred_train_comuna

    # Calculate mean squared error

    mse_residuos_comuna = mean_squared_error(y_train_comuna, y_pred_train_comuna)

    # Perform Shapiro-Wilk test for normality

    shapiro_test = stats.shapiro(residuos_comuna)

    # Perform Kolmogorov-Smirnov test for normality

    k2, p_value = stats.normaltest(residuos_comuna)

    # Add constant column to X_train

    X_with_constant = sm.add_constant(X_train_comuna[features_excluding_comuna])

    # Perform Breusch-Pagan test for heteroscedasticity

    lm, lm_p_value, fvalue, f_p_value = het_breuschpagan(residuos_comuna, X_with_constant)

    # Calculate pairwise Pearson correlations

    correlacion_comuna = calcular_correlacion_por_comuna(datos_comuna, features_excluding_comuna)

    # Store training results

    result = {
        'modelo_final': modelo_final,
        'X_train_selected': X_train_selected,
        'residuos_comuna': residuos_comuna,
        'mse_residuos_comuna': mse_residuos_comuna,
        'shapiro_test': shapiro_test,
        'k2': k2,
        'p_value': p_value,
        'lm': lm,
        'lm_p_value': lm_p_value,
        'fvalue': fvalue,
        'f_p_value': f_p_value,
        'y_pred_train_comuna': y_pred_train_comuna,
        'correlacion_comuna': correlacion_comuna,
        'len_train_comuna': len(y_train_comuna)
    } 

    return modelo_final, X_train_selected, residuos_comuna, y_train_comuna, result, X_train_comuna, features_excluding_comuna, sfs, X_test_comuna, y_test_comuna

    pass
