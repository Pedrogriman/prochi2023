# diagnostico.py
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

def plot_diagnostic_plots(y_true, y_pred, residuos, comuna):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10))

    # Scatter plot of predicted vs. true values

    axes[0, 0].scatter(y_true, y_pred, edgecolors=(0, 0, 0), alpha=0.6, label='Observations')
    axes[0, 0].plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'k--', lw=2, label='45° Line')
    axes[0, 0].set_title('Predicted vs. Actual Values', fontsize=12)
    axes[0, 0].set_xlabel('Actual')
    axes[0, 0].set_ylabel('Prediction')
    axes[0, 0].tick_params(labelsize=9)
    axes[0, 0].legend(fontsize=9)

    # Residual plot

    axes[0, 1].scatter(list(range(len(y_true))), residuos, edgecolors=(0, 0, 0), alpha=0.6, label='Residuals')
    axes[0, 1].axhline(y=0, linestyle='--', lw=2, label='Baseline')
    axes[0, 1].set_title('Model Residuals', fontsize=12)
    axes[0, 1].set_xlabel('ID')
    axes[0, 1].set_ylabel('Residual')
    axes[0, 1].tick_params(labelsize=9)
    axes[0, 1].legend(fontsize=9)

    # Histogram of residuals

    sns.histplot(
        data=residuos,
        stat="density",
        kde=True,
        line_kws={'linewidth': 1},
        alpha=0.5,
        ax=axes[1, 0]
    )
    axes[1, 0].set_title('Distribution of Model Residuals', fontsize=12)
    axes[1, 0].set_xlabel("Residual")
    axes[1, 0].tick_params(labelsize=9)

    # Q-Q plot

    sm.qqplot(residuos, fit=True, line='q', ax=axes[1, 1], alpha=0.6, lw=2)
    axes[1, 1].set_title('Q-Q Plot of Model Residuals', fontsize=12)
    axes[1, 1].tick_params(labelsize=9)

    # Scatter plot of residuals vs. predictions

    axes[2, 0].scatter(y_pred, residuos, edgecolors=(0, 0, 0), alpha=0.6, label='Residuals')
    axes[2, 0].axhline(y=0, linestyle='--', lw=2, label='Baseline')
    axes[2, 0].set_title('Model Residuals vs. Prediction', fontsize=12)
    axes[2, 0].set_xlabel('Prediction')
    axes[2, 0].set_ylabel('Residual')
    axes[2, 0].tick_params(labelsize=9)
    axes[2, 0].legend(fontsize=9)

    # Remove empty subplot

    fig.delaxes(axes[2, 1])

    fig.tight_layout()
    plt.subplots_adjust(top=0.95)
    fig.suptitle(f'Model Residual Diagnostics - {comuna}\n', fontsize=14)

    plt.show()

    pass
