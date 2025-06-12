import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
import numpy as np
from loadandcleandata import load

def plot():
    df = load()
    
    df = df.groupby('YearMonth', as_index=False)['TotalSalesAmount'].sum()
    df = df[['YearMonth', 'TotalSalesAmount']]
    df['ds'] = pd.to_datetime(df['YearMonth'], format='%Y%m')
    df = df.sort_values(by='ds')
    df = df[['ds', 'TotalSalesAmount']].rename(columns={'TotalSalesAmount': 'y'})
    df.dropna(inplace=True)
    
    #features
    df['ds'] = pd.to_datetime(df['ds'])
    df['dayofweek'] = df['ds'].dt.dayofweek
    df['day'] = df['ds'].dt.day
    df['month'] = df['ds'].dt.month
    df['year'] = df['ds'].dt.year

    # Train/test split
    train = df[(df['ds'] >= '2015-01-01') & (df['ds'] <= '2016-08-31')]
    test = df[(df['ds'] >= '2016-09-01') & (df['ds'] <= '2016-12-31')]

    features = ['dayofweek', 'day', 'month', 'year']
    X_train = train[features]
    y_train = train['y']
    X_test = test[features]
    y_test = test['y']

    # Train model
    model = xgb.XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Predict on test
    y_pred = model.predict(X_test)
    y_pred = np.maximum(0, y_pred)

    # Create DataFrame for predictions on test
    y_pred_df = pd.DataFrame({
        'ds': test['ds'].values,
        'y': y_pred
    })

    # Forecast future (2017)
    future_dates = pd.date_range(start='2017-01-01', end='2017-06-30')
    future_df = pd.DataFrame({'ds': future_dates})
    future_df['dayofweek'] = future_df['ds'].dt.dayofweek
    future_df['day'] = future_df['ds'].dt.day
    future_df['month'] = future_df['ds'].dt.month
    future_df['year'] = future_df['ds'].dt.year

    X_future = future_df[features]
    y_future = model.predict(X_future)
    y_future = np.maximum(0, y_future)

    future_pred_df = pd.DataFrame({
        'ds': future_df['ds'],
        'y': y_future
    })

    # Plot everything
    plt.figure(figsize=(14, 6))

    # 1. Actual
    plt.plot(test['ds'], y_test, label='Actual', color='black', alpha=0.5)

    # 2. Prediction on test set
    plt.plot(y_pred_df['ds'], y_pred_df['y'], label='XGBoost Prediction (Test)', color='blue', marker='o')

    # 3. Forecast for future
    plt.plot(future_pred_df['ds'], future_pred_df['y'], label='Forecast 2017', color='red', linestyle='--')

    plt.title('Actual vs Predicted vs Forecast (XGBoost)')
    plt.xlabel('Date')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Create a DataFrame to return predictions with dates
    # forecast_df = pd.DataFrame({
    #     'ds': test['ds'].values,
    #     'y': y_pred+1500
    # })
    
    return plt


def run_forecast():
    df = load()

    df = df.groupby('YearMonth', as_index=False)['TotalSalesAmount'].sum()
    df = df[['YearMonth', 'TotalSalesAmount']]
    df['ds'] = pd.to_datetime(df['YearMonth'], format='%Y%m')
    df = df.sort_values(by='ds')
    df = df[['ds', 'TotalSalesAmount']].rename(columns={'TotalSalesAmount': 'y'})
    df.dropna(inplace=True)

    df['ds'] = pd.to_datetime(df['ds'])
    df['dayofweek'] = df['ds'].dt.dayofweek
    df['day'] = df['ds'].dt.day
    df['month'] = df['ds'].dt.month
    df['year'] = df['ds'].dt.year

    # Train/test split
    train = df[(df['ds'] >= '2015-01-01') & (df['ds'] <= '2016-08-31')]
    test = df[(df['ds'] >= '2016-09-01') & (df['ds'] <= '2016-12-31')]

    features = ['dayofweek', 'day', 'month', 'year']
    X_train = train[features]
    y_train = train['y']
    X_test = test[features]
    y_test = test['y']

    # Train model
    model = xgb.XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Predict on test
    y_pred = model.predict(X_test)
    y_pred = np.maximum(0, y_pred)

    # Create DataFrame for predictions on test
    y_pred_df = pd.DataFrame({
        'ds': test['ds'].values,
        'y': y_pred
    })

    # Forecast future (2017)
    future_dates = pd.date_range(start='2017-01-01', end='2017-06-30')
    future_df = pd.DataFrame({'ds': future_dates})
    future_df['dayofweek'] = future_df['ds'].dt.dayofweek
    future_df['day'] = future_df['ds'].dt.day
    future_df['month'] = future_df['ds'].dt.month
    future_df['year'] = future_df['ds'].dt.year

    X_future = future_df[features]
    y_future = model.predict(X_future)
    y_future = np.maximum(0, y_future)

    
    #Create a DataFrame to return predictions with dates
    forecast_df = pd.DataFrame({
        'ds': future_df['ds'].values,
        'y': y_future
    })

    return forecast_df
    