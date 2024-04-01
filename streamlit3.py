import streamlit as st
import pandas as pd
import altair as alt

def main():
    # Title
    st.title("Patient Data Visualization")

    # Load the synthetic patient data
    synthetic_patient_data = pd.read_csv('synthetic_patient_data6.csv')

    # Convert the 'Year' and 'Month' columns to datetime
    synthetic_patient_data['YearMonth'] = pd.to_datetime(synthetic_patient_data['Year'].astype(str) + '-' + synthetic_patient_data['Month'].astype(str))

    # Filter data for years 2020 to 2024
    filtered_data = synthetic_patient_data[(synthetic_patient_data['Year'] >= 2020) & (synthetic_patient_data['Year'] <= 2024)]

    # Melt the dataframe to have a single 'value' column for patient counts
    melted_data = pd.melt(filtered_data, id_vars=['YearMonth'], value_vars=['Italy', 'Spain', 'US'], var_name='Country', value_name='Active Patients')

    # Line chart for active patients over time
    st.subheader("Active Patients Over Time (2020-2024)")
    chart = alt.Chart(melted_data).mark_line().encode(
        x=alt.X('YearMonth:T', title='Year'),
        y=alt.Y('Active Patients:Q', title='Total Active Patients'),
        color='Country:N'
    ).properties(
        width=800,
        height=500
    )

    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()


