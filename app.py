import streamlit as st
import random
import time
import pandas as pd


st.title(":orange[India]CSRankings ")
st.header("Rankings based on A/A* Conferences:")

file = r'C:\Users\Rishikesh\BITS\Hackenza\college_ranking_A.csv'

if file is not None:
    # Step 2: Read the CSV file into a DataFrame
    data = pd.read_csv(file)
    
    # Step 3: Display the DataFrame
    st.dataframe(data, use_container_width=True)
    
    # Optional: Allow users to download the CSV file
    st.download_button(
        label="Download CSV",
        data=data.to_csv(index=False),
        file_name='dataframe.csv',
        mime='text/csv',
    )

st.header("Rankings based on Q1 Journals:")

file = r'C:\Users\Rishikesh\BITS\Hackenza\college_ranking_q1.csv'

if file is not None:
    # Step 2: Read the CSV file into a DataFrame
    data = pd.read_csv(file)
    
    # Step 3: Display the DataFrame
    st.dataframe(data, use_container_width=True)
    
    # Optional: Allow users to download the CSV file
    st.download_button(
        label="Download CSV",
        data=data.to_csv(index=False),
        file_name='dataframe.csv',
        mime='text/csv',
    )

st.title(":Red[Raw]Data")
st.header("Scraped Data Dump of all A/A* conferences and Q1 Journals: ")

file = r'C:\Users\Rishikesh\BITS\Hackenza\2023_data.csv'

if file is not None:
    # Step 2: Read the CSV file into a DataFrame
    data = pd.read_csv(file)
    
    # Step 3: Display the DataFrame
    st.dataframe(data, use_container_width=True)
    
    # Optional: Allow users to download the CSV file
    st.download_button(
        label="Download CSV",
        data=data.to_csv(index=False),
        file_name='dataframe.csv',
        mime='text/csv',
    )
