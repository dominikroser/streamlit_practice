import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Function to generate synthetic patient data for each country
def generate_synthetic_patient_data(country):
    if country == 'USA':
        initial_patients = 10000
        monthly_increase_min = 200
        monthly_increase_max = 500
    else:
        initial_patients = 100
        monthly_increase_min = 50
        monthly_increase_max = 100
    
    # Generate synthetic patient data
    dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='M')
    patients = [initial_patients]
    for i in range(len(dates) - 1):
        increase = np.random.randint(monthly_increase_min, monthly_increase_max + 1)
        patients.append(patients[-1] + increase)
    df = pd.DataFrame({'Date': dates, 'Patients': patients, 'Country': country})
    return df

def main():
    # Title
    st.title("Patient Data Visualization")

    # Sidebar for user inputs
    st.sidebar.title('Filters')
    selected_country = st.sidebar.selectbox('Select Country', ['USA', 'Italy', 'Spain'])

    # Generate synthetic patient data based on selected country
    patient_data = generate_synthetic_patient_data(selected_country)

    # Line chart for patients over time
    st.subheader(f"Patients Over Time ({selected_country})")
    chart = alt.Chart(patient_data).mark_line().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Patients:Q', title='Patients'),
        color='Country:N'
    ).properties(
        width=800,
        height=500
    )

    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()
