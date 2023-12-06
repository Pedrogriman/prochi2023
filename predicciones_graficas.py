# predicciones_graficas.py
import pandas as pd

def make_predictions_and_plot(y_test_comuna, modelo_final, sfs, X_test_comuna, features_excluding_comuna, comuna, predictions_by_comuna):
    # Check if there are samples in the testing data for the given commune

    if X_test_comuna[features_excluding_comuna].shape[0] == 0:
        print(f"No samples in the testing data for {comuna}. Skipping predictions and plot.")
        return predictions_by_comuna, None, None

    # Filter testing data for the given commune

    X_test_comuna = X_test_comuna[X_test_comuna['Comuna'] == comuna]

    # Add intercept column to the testing data for the given commune

    X_test_comuna = sm.add_constant(X_test_comuna, prepend=True).rename(columns={'const': 'intercept'})

    # Check if there are features for the given commune

    if X_test_comuna[features_excluding_comuna].shape[1] == 0:
        print(f"No features for {comuna}. Skipping predictions and plot.")
        return predictions_by_comuna, None, None

    # Make predictions for the given commune

    y_pred_comuna = modelo_final.predict(sfs.transform(X_test_comuna[features_excluding_comuna]))

    # Add predictions to the accumulated DataFrame

    predictions_by_comuna = predictions_by_comuna.append(
        pd.DataFrame({'comuna': comuna, 'true_value': y_test_comuna, 'predicted_value': y_pred_comuna}))

    # Generate diagnostic plots for the given commune

    fig, axes = plot_diagnostic_plots(y_test_comuna, y_pred_comuna, y_test_comuna - y_pred_comuna, comuna)


    return predictions_by_comuna, fig, axes
    pass
