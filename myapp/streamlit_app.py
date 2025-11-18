import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Some data")
    df = pd.read_csv("dataset.csv")
    ff = px.scatter(df, x="DATE", y="TEMP")
    st.plotly_chart(ff, use_container_width=True)

if __name__ == "__main__":
    main()


