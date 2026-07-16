
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Afficionado Coffee Dashboard', layout='wide')
st.title('☕ Afficionado Coffee Roasters: Operations Dashboard')

st.sidebar.header('Settings')
store = st.sidebar.selectbox('Select Store Location', ['Astoria', "Hell's Kitchen", 'Lower Manhattan'])

st.header(f'Insights for {store}')

# Dynamic metrics based on our analysis
mae_map = {'Astoria': 248.48, "Hell's Kitchen": 264.93, 'Lower Manhattan': 231.61}

col1, col2, col3 = st.columns(3)
col1.metric('Model MAE', f'${mae_map[store]}')
col2.metric('Peak Hour', '10:00 AM')
col3.metric('Data Horizon', '6 Months')

st.subheader('Strategic Recommendation')
st.success(f'Based on hourly analysis, {store} should optimize labor shifts for the 07:00-11:00 window.')

# Placeholder for charts - in a live app, you would pass the dataframes here
st.info('The interactive charts below would display the Prophet forecast and hourly distributions generated in the analysis.')
