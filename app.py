import streamlit as st
from forecast import plot as plot_sales, run_forecast
from itemforecast import plot_item, run_forecast_item
from config import insert_forecast_to_mssql, insert_forecast_item_to_mssql
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Forecast Uploader", layout="centered")
st.title("📈 Forecast Upload to MSSQL")

# Initialize session state variables
if 'forecast_sales_ready' not in st.session_state:
    st.session_state.forecast_sales_ready = False
if 'forecast_item_ready' not in st.session_state:
    st.session_state.forecast_item_ready = False

# ---------- SECTION 1: Forecast Sales ----------
st.header("🧾 Forecast Sales")

if st.button("🔁 Run Forecast Sales"):
    st.info("Running forecast for sales...")
    st.session_state.forecast_df_sales = run_forecast()
    st.session_state.forecast_sales_ready = True
    st.success("✅ Forecast for sales completed.")

if st.session_state.forecast_sales_ready:
    st.subheader("📊 Sales Forecast Visualization")
    fig = plot_sales()
    st.pyplot(fig)

    if st.button("✅ Confirm Upload Sales Forecast to SQL Server"):
        insert_forecast_to_mssql(st.session_state.forecast_df_sales)
        st.success("📥 Sales Forecast Uploaded to MSSQL Successfully!")

st.markdown("---")

# ---------- SECTION 2: Forecast Item ----------
st.header("📦 Forecast Item")

if st.button("🔁 Run Forecast Item"):
    st.info("Running forecast for items...")
    st.session_state.forecast_df_item = run_forecast_item()
    st.session_state.forecast_item_ready = True
    st.success("✅ Forecast for items completed.")

if st.session_state.forecast_item_ready:
    st.subheader("📊 Item Forecast Visualization")
    fig = plot_item()
    st.pyplot(fig)

    if st.button("✅ Confirm Upload Item Forecast to SQL Server"):
        insert_forecast_item_to_mssql(st.session_state.forecast_df_item)
        st.success("📥 Item Forecast Uploaded to MSSQL Successfully!")

st.markdown("---")
