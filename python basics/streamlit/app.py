import streamlit as st # to run this file you have to first go in the streamlit folder dir by using cd pythonbasics then cd streamlit then streamlit run app.py. we do this cuz here streamlit used. even tho if you changed your python interpreter to cond venv still ctrl+alt+n will show error in running this file 
import numpy as np
import pandas as pd

st.title("Hello Streamlit")
st.write("This is my first streamlit app")

name=st.text_input("Enter Your Name: ")
st.write(f"Your Name is {name}")

# making a slider where you can select you age by dragging the cursor
age=st.slider("Enter Your Age: ",0,100,25)         # this 25 is base age like cursor on defualt first points to 25
st.write(f"Your Age Is {age}")

# Making options and giving options in selectbox to make a dropdown. and then st.write
options=["C++","Python","C","Java"]
lang=st.selectbox("Choose Your Favourite Language: ",options)
st.write(f"Your Favourite Language is: {lang}")

# writing dataframe using streamlit
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
st.write(df)

df.to_csv("sample_data.CSV") # sample_data.CSV will be the name of csv file 

# using fileuploader so that user can provide any dataset CSV file to display it using st.write
uploaded_file=st.file_uploader("Choose a File below ",type="csv")

if uploaded_file is not None:
   dff=pd.read_csv(uploaded_file) # using pandas to read csv file already converts the data into dataframe.
   st.write(dff)


