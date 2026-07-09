from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score


def evaluate_model(model, X, y):
    preds = model.predict(X)
    
    mae = mean_absolute_error(y, preds)
    rmse = root_mean_squared_error(y, preds)
    r2 = r2_score(y, preds)
    
    print(f"MAE: {mae:.2f} RMSE: {rmse:.2f} R2 score: {r2:.2f}")

    return {'mae': mae, 'rmse': rmse, 'r2_score': r2}
    