import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import numpy as np

def handle_null_values(data, method, fill_value=None):
    if method == 'drop':
        data = data.dropna()
    elif method == 'mean':
        imputer = SimpleImputer(strategy='mean')
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif method == 'median':
        imputer = SimpleImputer(strategy='median')
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif method == 'mode':
        imputer = SimpleImputer(strategy='most_frequent')
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif method == 'constant':
        data = data.fillna(fill_value)
    elif method == 'forward_fill':
        data = data.ffill()
    elif method == 'backward_fill':
        data = data.bfill()
    return data

def handle_categorical_columns(data):
    for column in data.columns:
        if data[column].dtype == 'object':
            label_encoder = LabelEncoder()
            data[column] = label_encoder.fit_transform(data[column])
    return data

def visualize_histogram(data):
    feature = st.selectbox('Select a feature to visualize:', data.columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(data[feature], kde=True)
    plt.title(f'Histogram of {feature}')
    st.pyplot(plt.gcf())

def main():
    st.title('Automated Data Cleaning and Visualisation Tool')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())

        null_handling_method = st.selectbox(
            'Select how to handle null values:',
            ('Drop', 'Mean', 'Median', 'Mode', 'Constant', 'Forward Fill', 'Backward Fill')
        )

        if null_handling_method == 'Constant':
            fill_value = st.number_input("Enter constant value for imputation:", value=0.0)
            data = handle_null_values(data, null_handling_method, fill_value)
        else:
            data = handle_null_values(data, null_handling_method)

        st.write("After handling null values:")
        st.write(data.head())

        categorical_columns = st.multiselect(
            'Select categorical columns to encode:',
            data.columns
        )
        if categorical_columns:
            for column in categorical_columns:
                data[column] = LabelEncoder().fit_transform(data[column])
            st.write("After encoding categorical columns:")
            st.write(data.head())

        st.header('Data Visualization')
        visualization_type = st.selectbox('Select type of visualization:', ('Histogram', 'Pie Chart'))
        if visualization_type == 'Histogram':
            visualize_histogram(data)
       
        st.download_button(
            label="Download preprocessed data",
            data=data.to_csv(index=False),
            file_name='preprocessed_data.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()