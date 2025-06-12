import pyodbc
import pandas as pd
from sqlalchemy import create_engine,text

def insert_forecast_to_mssql(forecast_df):
    conn_str = create_engine(
        "mssql+pyodbc://U_user:abc123+@127.0.0.1:1433/AXDW"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    create_table_sql = """
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
    """

    # ใช้ engine.begin() เพื่อเปิด transaction
    with conn_str.begin() as conn:
        conn.execute(text(create_table_sql))

    forecast_df.to_sql(
        name='FORECASTSALESAMOUNTBYDATE',  # ชื่อตาราง
        con=conn_str,
        if_exists='replace',                # หรือ 'replace' เพื่อเขียนทับ
        index=False                        # ไม่เอา index ลงตาราง
    )


def insert_forecast_item_to_mssql(forecast_df):
    conn_str = create_engine(
        "mssql+pyodbc://U_user:abc123+@127.0.0.1:1433/AXDW"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    create_table_sql = ("""
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
    with conn_str.begin() as conn:
        conn.execute(text(create_table_sql))

    forecast_df.to_sql(
        name='FORECASTITEMBYDATE',  # ชื่อตาราง
        con=conn_str,
        if_exists='replace',                # หรือ 'replace' เพื่อเขียนทับ
        index=False                        # ไม่เอา index ลงตาราง
    )


def fetch_forecast_from_mssql():

    conn_str = (
        "mssql+pyodbc://U_user:abc123+@127.0.0.1:1433/AXDW"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    
    query = "SELECT * FROM [dbo].[AggMonthlySalesInvoiceLine4]"
    df = pd.read_sql(query, conn_str)
    
    return df



