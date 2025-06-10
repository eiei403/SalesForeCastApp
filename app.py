import streamlit as st
from forecast import run_forecast
from itemforecast import run_forecast_item
from config import insert_forecast_to_mssql
from config import insert_forecast_item_to_mssql
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Forecast Uploader", layout="centered")
st.title("📈 Forecast to MSSQL")

if st.button("🔁 Run Forecast Sales & Upload"):
    st.info("Running forecast...")
    forecast_df = run_forecast()
    
    st.subheader("🔍 Preview Forecast Data")
    # st.dataframe(forecast_df)
    st.dataframe(forecast_df.head(10))

    # Visualize
    st.subheader("📊 Forecast Visualization")
    plt.figure(figsize=(12,6))
    plt.plot(forecast_df['ds'], forecast_df['y'], label='XGBoost Forecast', marker='x')
    plt.title('Forecast (XGBoost)')
    plt.legend()
    plt.grid()
    plt.tight_layout()

    st.pyplot(plt)

    #confirm upload
    if st.button("✅ Confirm Upload to SQL Server"):
        insert_forecast_to_mssql(forecast_df)
        st.success("📥 Uploaded to MSSQL Successfully!")

    #st.info("Uploading to MSSQL...")
    #insert_forecast_to_mssql(forecast_df)

    #st.success("✅ Forecast uploaded successfully!")

if st.button("🔁 Run Forecast Items & Upload"):
    st.info("Running forecast...")
    forecast_df = run_forecast_item()
    
    st.subheader("🔍 Preview Forecast Data")
    # st.dataframe(forecast_df)
    st.dataframe(forecast_df.head(10))

    # Visualize
    st.subheader("📊 Forecast Item Visualization")
    plt.figure(figsize=(12,6))
    plt.plot(forecast_df['ds'], forecast_df['y'], label='XGBoost Forecast', marker='x')
    plt.title('Forecast (XGBoost)')
    plt.legend()
    plt.grid()
    plt.tight_layout()

    st.pyplot(plt)

    #confirm upload
    if st.button("✅ Confirm Upload to SQL Server"):
        insert_forecast_item_to_mssql(forecast_df)
        st.success("📥 Uploaded to MSSQL Successfully!")

    #st.info("Uploading to MSSQL...")
    #insert_forecast_to_mssql(forecast_df)

    #st.success("✅ Forecast uploaded successfully!")
    
