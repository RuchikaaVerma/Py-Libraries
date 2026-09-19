import streamlit as st
import pandas as pd
import numpy as np
#Title of the application
st.title("Hello Streamlit")
#Display Simple text
st.write("This is sample Text")
#create a dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
#Display the dataframe
st.write("This is sample DataFrame")
st.dataframe(df)

#Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
chart_data=pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
    
)

st.line_chart(chart_data)
