import streamlit as st
import pandas as pd
from pandas import DataFrame

def sidebar(df: DataFrame):
    sidebarInputs = [''] * len(df.columns)
    sidebarStatements = [i for i in df.columns]
    with st.sidebar:
        for i in range(len(df.columns)):
            sidebarInputs[i] = st.chat_input(sidebarStatements[i])
        # reset = st.button("Reset Filters")
    return [sidebarInputs, sidebarStatements]


def layout():
    st.set_page_config(layout="wide")
    st.title("Job Search Application Manager", text_alignment="center")

    df = pd.read_csv("applications.csv")

    editedDF = st.data_editor(df, num_rows="dynamic")
    csv = editedDF.to_csv()

    st.download_button(label="Download File as CSV", data=csv, file_name="applications.csv", mime="text/csv")


layout()