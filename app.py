import streamlit as st
import pandas as pd
import plotly.express as px
st.title('Análisis Exploratorio de Datos de Vehículos')

st.header('Datos de Vehículos de EE.UU.')

car_data = pd.read_csv('notebooks/vehicles_us.csv')

if st.button('Mostrar Histograma del Año de los Vehículos'):
    st.write("Histograma del año de los vehículos:")
    fig = px.histogram(car_data, x='model_year')
    st.plotly_chart(fig)

if st.button('Mostrar Gráfico de Dispersión Precio vs Millaje'):
    st.write("Gráfico de dispersión del precio vs millaje de los vehículos:")
    scatter_fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(scatter_fig)
