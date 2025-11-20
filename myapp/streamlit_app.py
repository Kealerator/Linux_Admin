import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px


@st.cache_resource
def mySql():

    # Print available secrets for debugging
    # st.write("Available secrets:", st.secrets)


    # Retrieve connection details from secrets
    host = st.secrets["connections"]["mysql"]["host"]
    user = st.secrets["connections"]["mysql"]["username"]
    password = st.secrets["connections"]["mysql"]["password"]
    database = st.secrets["connections"]["mysql"]["database"]


    # Initialize connection.
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Perform query to fetch all data from the 'People' table.
        query = 'SELECT * FROM People;'
        df = pd.read_sql(query, conn)

        return df

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None
    finally:
        if conn:
            conn.close()

# Streamlit main function
def main():
    st.title("View Data from MySQL")
    st.write("Displaying all data from the People table")

    # Fetch data
    data = mySql()
    
    # Create DataFrame
    if data is not None:
        st.dataframe(data)

        # Optional: Plot data if you have numerical columns
        if 'SomeNumericalColumn' in data.columns:  # Replace with actual column name if needed
            line_chart = px.line(data, x=data.index, y='SomeNumericalColumn')  # Adjust column name as needed
            st.plotly_chart(line_chart, use_container_width=True)

if __name__ == "__main__":
    main()

