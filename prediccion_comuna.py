# prediccion_comuna.py
import pandas as pd

def calculate_predictions_by_comuna(comuna, modelo_final, sfs, X_test_comuna, features_excluding_comuna, y_test_comuna):
    # Transform only if there are samples
    X_test_comuna_selected = sfs.transform(X_test_comuna[features_excluding_comuna])

    # Initialize predictions_by_comuna DataFrame
    predictions_by_comuna = pd.DataFrame()

    # Check if there are features after transformation
    if X_test_comuna_selected.shape[1] == 0:
        print(f"No features after transformation for {comuna}. Skipping predictions and plot.")
        return predictions_by_comuna, None, None

    # Make predictions
    predictions_comuna = modelo_final.predict(X_test_comuna_selected)
    
    # Create a DataFrame with predictions, including ID and Comuna
    predictions_comuna_df = pd.DataFrame({'Comuna': comuna, 'Predictions': predictions_comuna})

    # Concatenate predictions to the overall DataFrame
    predictions_by_comuna = pd.concat([predictions_by_comuna, predictions_comuna_df], ignore_index=True)

    # Adjust the RMSE calculation based on your specific requirements
    error = rmse(y_test_comuna.values.flatten(), predictions_by_comuna['Predictions'].values)

    return predictions_by_comuna, predictions_comuna_df, error
    pass
