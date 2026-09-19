import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name=st.text_input("Enter your name","Type here ...")
if name:
    st.write(f"Hello,{name}")
    age=st.number_input("Enter your age",0,130,25)
    st.write(f"Your age is {age}.")
    options =["python","Java","C++","Ruby"]
    choice=st.selectbox("Choose your favorite programming language",options)
    st.write(f"You selected {choice}.")
    if name:
        st.write(f"Your name is {name} and your age is {age}")
data={
    'Name':["John","Jane","Doe"],
    'Age':[28,34,29],
    'City':["New York","San Francisco","Los Angeles"]
    
}
df=pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    