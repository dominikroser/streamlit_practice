import streamlit as st
import pandas as pd
import altair as alt

# Load the synthetic patient data
synthetic_patient_data = pd.read_csv('synthetic_patient_data6.csv')

# Sidebar for user inputs
st.sidebar.title('Filters')
selected_country = st.sidebar.selectbox('Select Country', ['Italy', 'Spain', 'US'])

# Filter data based on selected country
filtered_data = synthetic_patient_data[synthetic_patient_data['Country'] == selected_country]

# Line chart for active patients over time
st.subheader(f'Active Patients in {selected_country}')
chart = alt.Chart(filtered_data).mark_line().encode(
    x='Month:T',
    y='Total Active Patients:Q',
    tooltip=['Month:T', 'Total Active Patients:Q']
).properties(
    width=600,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_legend(
    titleFontSize=14,
    labelFontSize=12
)

st.altair_chart(chart, use_container_width=True)
