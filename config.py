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
    cursor.execute("""
        IF NOT EXISTS (
            SELECT * FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'FORECASTSALESAMOUNTBYDATE'
        )
        BEGIN
            CREATE TABLE [dbo].[FORECASTSALESAMOUNTBYDATE] (
                ds DATE NOT NULL,
                y FLOAT
            )
        END
        """)
    conn.commit()

    for _, row in forecast_df.iterrows():
        cursor.execute(
            "INSERT INTO [dbo].[FORECASTSALESAMOUNTBYDATE] (ds, y) VALUES (?, ?)",
            row['ds'], row['y']
        )

    conn.commit()
    cursor.close()
    conn.close()


def insert_forecast_item_to_mssql(forecast_df):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=127.0.0.1,1433;'
        'DATABASE=AXDW;'
        'UID=U_user;'
        'PWD=abc123+',
        timeout=10
    )
    cursor = conn.cursor()
    cursor.execute("""
        IF NOT EXISTS (
            SELECT * FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'FORECASTITEMBYDATE'
        )
        BEGIN
            CREATE TABLE [dbo].[FORECASTITEMBYDATE] (
                ds DATE NOT NULL,
                y FLOAT
            )
        END
        """)
    conn.commit()

    for _, row in forecast_df.iterrows():
        cursor.execute(
            "INSERT INTO [dbo].[FORECASTITEMBYDATE] (ds, y) VALUES (?, ?)",
            row['ds'], row['y']
        )

    conn.commit()
    cursor.close()
    conn.close()
