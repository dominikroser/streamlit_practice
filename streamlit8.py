import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Function to generate synthetic patient data for each country
def generate_synthetic_patient_data(countries, start_date, end_date):
    data = []
    for country in countries:
        if country == 'USA':
            initial_patients = 10000
            initial_active_patients = 5000
            monthly_increase_min = 200
            monthly_increase_max = 500
        else:
            initial_patients = 100
            initial_active_patients = 40
            monthly_increase_min = 50
            monthly_increase_max = 100
        
        # Generate synthetic patient data
        dates = pd.date_range(start=start_date, end=end_date, freq='M')
        patients = [initial_patients]
        active_patients = [initial_active_patients]
        for i in range(len(dates) - 1):
            increase = np.random.randint(monthly_increase_min, monthly_increase_max + 1)
            patients.append(patients[-1] + increase)
            active_patients.append(active_patients[-1] + increase - np.random.randint(0, increase // 2))
        country_data = pd.DataFrame({'Date': dates, 'Patients': patients, 'Active Patients': active_patients, 'Country': country})
        data.append(country_data)
    return pd.concat(data)


def generate_synthetic_OMG_data(countries, start_date, end_date):
    data = []
    for country in countries:
        if country == 'Spain':
            initial_patients = 1000
            initial_active_patients = 500
            monthly_increase_min = 50
            monthly_increase_max = 200
        else:
            initial_patients = 5000
            initial_active_patients = 900
            monthly_increase_min = 100
            monthly_increase_max = 400
        
        # Generate synthetic patient data
        dates = pd.date_range(start=start_date, end=end_date, freq='M')
        patients = [initial_patients]
        active_patients = [initial_active_patients]
        for i in range(len(dates) - 1):
            increase = np.random.randint(monthly_increase_min, monthly_increase_max + 1)
            patients.append(patients[-1] + increase)
            active_patients.append(active_patients[-1] + increase - np.random.randint(0, increase // 2))
        country_data = pd.DataFrame({'Date': dates, 'Patients': patients, 'Active Patients': active_patients, 'Country': country})
        data.append(country_data)
    return pd.concat(data)

def business_insights():
    # Title
    st.title("Business Insights")
    
    #Welcome message
    st.write("Welcome to the Business statistics visualization dashboard. This dashboard provides insights into the patient data for different applications")
    
    # Sidebar for user inputs
    st.sidebar.title('Filters')
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('2020-01-01'))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('2024-12-31'))
    
    selected_application = st.sidebar.selectbox('Select application', ['KNX', 'OMG'])
    
    countries = ['USA', 'Italy', 'Spain']
    
    if selected_application == 'KNX':
        patient_data = generate_synthetic_patient_data(countries, start_date, end_date)
    else:
        patient_data = generate_synthetic_OMG_data(countries, start_date, end_date)

    # Line chart for patients over time
    st.subheader("Patients Over Time")
    patient_chart = alt.Chart(patient_data).mark_line().encode(
        x=alt.X('year(Date):O', title='Date', axis=alt.Axis(format='%Y - %m', labelAngle=0)),
        y=alt.Y('Patients:Q', title='Patients'),
        color='Country:N'
    ).properties(
        width=900,
        height=500
    )
    st.altair_chart(patient_chart, use_container_width=True)

    # Line chart for active patients over time
    st.subheader("Active Patients Over Time")
    active_patient_chart = alt.Chart(patient_data).mark_line().encode(
        x=alt.X('year(Date):O', title='Date', axis=alt.Axis(format='%Y - %m', labelAngle=0)),
        y=alt.Y('Active Patients:Q', title='Active Patients'),
        color='Country:N'
    ).properties(
        width=900,
        height=500
    )
    st.altair_chart(active_patient_chart, use_container_width=True)

def operations():
    # Title
    st.title("Operations")
    st.write("This page will contain operations related information.")

def main():
    # Sidebar for page selection
    page = st.sidebar.radio("Select a page", ["Business Insights", "Operations"])

    if page == "Business Insights":
        business_insights()
    elif page == "Operations":
        operations()

if __name__ == "__main__":
    main()

