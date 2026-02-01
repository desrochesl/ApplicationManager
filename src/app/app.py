import streamlit as st
import pandas as pd
from pandas import DataFrame

# TODO: 
# '''
# Formatting:
# Title
# DF
# Load from/to .db or .csv
    
# Button for uploading to df
#     Switch statement to handle if it is a .csv or .db or else

# Ways to filter Data:
#     Select a column and user inputs data they want to filter by

# Social Links

# Button to save changes

# '''

def layout(df: DataFrame):
    st.title("Job Search Application Manager", text_alignment="center")
    # st.subheader("") # Not sure what I want this for yet
    # st.file_uploader() # Needs fixing

    # Make two colums and put both buttons on the same line
    # st.download_button("Download to CSV")
    # st.download_button("Download to DB")

    original = df

    
    with st.sidebar:
        x = st.chat_input("Test")
        reset = st.button("Reset Filters")
    if x:
        df = df[df["command"] == x]

    

    editedData = st.data_editor(df)
    saveChanges = st.button("Save changes")

    if saveChanges:
            print(editedData)
            df = editedData
            ...

    if reset:
        ...
        


df = pd.DataFrame(
    [
        {"command": "st.dataframe", "rating": 4, "is_widget": False},
        {"command": "st.data_editor", "rating": 5, "is_widget": True},
        {"command": "st.table", "rating": 3, "is_widget": False},
        {"command": "st.metric", "rating": 5, "is_widget": True},
    ]
)

layout(df)


