# vif.py
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(X_train_comuna, features_excluding_comuna, comuna):
    vif_by_comuna = pd.DataFrame()

    # Check if the array has at least two dimensions and more than one element

    if X_train_comuna[features_excluding_comuna].values.ndim >= 2 and X_train_comuna[features_excluding_comuna].values.size > 1:

        # Calculate the VIF for each predictor variable
        vif_comuna = [variance_inflation_factor(X_train_comuna[features_excluding_comuna].values, i) for i in range(len(features_excluding_comuna))]

        # Create a DataFrame with the VIF results
        vif_comuna_df = pd.DataFrame({"variables": features_excluding_comuna, "VIF": vif_comuna})
        vif_comuna_df["Comuna"] = comuna

        # Add the DataFrame to the results
        vif_by_comuna = pd.concat([vif_by_comuna, vif_comuna_df], ignore_index=True)

    return vif_by_comuna
    pass
