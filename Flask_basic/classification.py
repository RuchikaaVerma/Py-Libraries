import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache the data loading
@st.cache_data
def load_data():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')
    target_names = iris.target_names
    return X, y, target_names

# Load dataset
df, target, target_names = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df, target)

# Sidebar UI
st.sidebar.title("🌸 Iris Flower Prediction")
sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    float(df["sepal length (cm)"].min()),
    float(df["sepal length (cm)"].max()),
    float(df["sepal length (cm)"].mean())
)
sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    float(df["sepal width (cm)"].min()),
    float(df["sepal width (cm)"].max()),
    float(df["sepal width (cm)"].mean())
)
petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    float(df["petal length (cm)"].min()),
    float(df["petal length (cm)"].max()),
    float(df["petal length (cm)"].mean())
)
petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    float(df["petal width (cm)"].min()),
    float(df["petal width (cm)"].max()),
    float(df["petal width (cm)"].mean())
)

# Prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
prediction_species = target_names[prediction[0]]

# Display results
st.subheader("🌼 Prediction Result")
st.write(f"Predicted Iris species: **{prediction_species.capitalize()}**")
