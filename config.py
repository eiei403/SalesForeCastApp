import pyodbc

def insert_forecast_to_mssql(forecast_df):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=127.0.0.1,1433;'
        'DATABASE=AXDW;'
        'UID=U_user;'
        'PWD=abc123+',
        timeout=10
    )
    cursor = conn.cursor()

    for _, row in forecast_df.iterrows():
        cursor.execute(
            "INSERT INTO [dbo].[FORECASTSALESAMOUNTBYDATE] (ds, y) VALUES (?, ?)",
            row['ds'], row['y']
        )

    conn.commit()
    cursor.close()
    conn.close()
