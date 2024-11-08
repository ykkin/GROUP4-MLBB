import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import networkx as nx
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.semi_supervised import LabelPropagation
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer


st.title('MACHINE LEARNING - Mobile Legends: Bang Bang E-sports Heroes Stats')


# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["About", "Dataset", "Value Counts", "EDA", "Machine Learning", "Conclusion", "Members"]
selected_section = st.sidebar.radio("Go to", sections)

# Title
st.title("MLBB Dashboard")

# About Section
if selected_section == "About":
    st.header("About")
    st.write("""
    Welcome to the MLBB (Mobile Legends: Bang Bang) Dashboard. This dashboard provides insights and 
    analytics on the statistics of various MLBB heroes, exploring key trends and applying machine learning 
    techniques to enhance gameplay strategies.
    """)

# Dataset Section
elif selected_section == "Dataset":
    st.header("Dataset")
    st.write("Here is a preview of the dataset used in this analysis.")
    df = pd.read_csv("Mlbb_Heroes.csv")
    df
    st.dataframe(df.head())

# Value Counts Section
elif selected_section == "Value Counts":
    st.header("Value Counts")
    column = st.selectbox("Select a column to view value counts:", df.columns)
    st.write(f"Value counts for {column}:")
    st.write(df[column].value_counts())

# Exploratory Data Analysis (EDA) Section
elif selected_section == "EDA":
    st.header("Exploratory Data Analysis (EDA)")
    st.write("Here, we explore the dataset through various visualizations.")

    # Example Visualization - Distribution of a numerical column
    numeric_column = st.selectbox("Select a numerical column to plot:", df.select_dtypes(include=['float', 'int']).columns)
    st.write(f"Distribution of {numeric_column}:")
    fig, ax = plt.subplots()
    sns.histplot(df[numeric_column], kde=True, ax=ax)
    st.pyplot(fig)

    # Scatter Plot
    st.write("Scatter Plot of two variables")
    col1, col2 = st.columns(2)
    x_col = col1.selectbox("Select X-axis:", df.select_dtypes(include=['float', 'int']).columns)
    y_col = col2.selectbox("Select Y-axis:", df.select_dtypes(include=['float', 'int']).columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    st.pyplot(fig)

# Machine Learning Section
elif selected_section == "Machine Learning":
    st.header("Machine Learning")
    st.write("This section applies machine learning models to the dataset.")

    # Example - Naive Bayes Classification (fill in with appropriate ML model as per your dataset)
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score

    # Assuming there is a target column (replace 'target_column' with actual column name)
    if 'target_column' in df.columns:
        X = df.drop('target_column', axis=1)  # Features
        y = df['target_column']  # Target

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Naive Bayes Model
        model = MultinomialNB()
        model.fit(X_train, y_train)
        
        # Predict and display accuracy
        y_pred = model.predict(X_test)
        st.write("Accuracy:", accuracy_score(y_test, y_pred))
    else:
        st.write("Please update with the correct target column.")

# Conclusion Section
elif selected_section == "Conclusion":
    st.header("Conclusion")
    st.write("""
    This concludes our analysis of MLBB hero statistics. The insights and model predictions here can 
    aid in better understanding hero characteristics and strategic choices in gameplay.
    """)

# Members Section
elif selected_section == "Members":
    st.header("Members")
    st.write("""
    - Edelle Lumabi
    - John Larence Lusaya
    - Nick Pastiu
    - Sophia Vitug
    - Daniel Santillan
    """)

