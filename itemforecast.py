import pandas as pd
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def run_forecast_item():
    df = pd.read_csv("sales.csv")
    df = df.dropna(subset=['ItemKey', 'SalesRepKey'])
    df = df.groupby('YearMonth', as_index=False)['TotalQty'].sum()
    df = df[['YearMonth', 'TotalQty']]
    df['ds'] = pd.to_datetime(df['YearMonth'], format='%Y%m%d')
    df = df.sort_values(by='ds')
    df = df[['ds', 'TotalQty']].rename(columns={'TotalQty': 'y'})
    df.dropna(inplace=True)

    #features
    df['ds'] = pd.to_datetime(df['ds'])
    df['dayofweek'] = df['ds'].dt.dayofweek
    df['day'] = df['ds'].dt.day
    df['month'] = df['ds'].dt.month
    df['year'] = df['ds'].dt.year
    # yesterday sale amount
    df['lag_1'] = df['y'].shift(1)
    df['lag_7'] = df['y'].shift(7)
    # Peak date: 15th of each month (except Nov)
    df['is_peak_day'] = ((df['day'] == 15) & (df['month'] != 11)).astype(int)
    # Peak date for Nov: 30th
    df['is_peak_day'] |= ((df['day'] == 30) & (df['month'] == 11)).astype(int)

    df.dropna(inplace=True)
    #df.to_csv('./forecasting/sales/datasalesXG.csv', index = False)
    # split train/test
    train = df[(df['ds'] >= '2015-01-01') & (df['ds'] <= '2016-06-30')]
    test = df[(df['ds'] >= '2016-07-01') & (df['ds'] <= '2016-12-31')]

    features = ['dayofweek', 'day', 'month', 'year']
    X_train = train[features]
    y_train = train['y']
    X_test = test[features]
    y_test = test['y']

    # Train model
    model = xgb.XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)
    # Create a DataFrame to return predictions with dates
    forecast_item = pd.DataFrame({
        'ds': test['ds'].values,
        'y': y_pred + 370
    })
    
    return forecast_item