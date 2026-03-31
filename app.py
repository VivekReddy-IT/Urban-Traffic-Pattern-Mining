import streamlit as st
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")

# Preprocessing
df['date_time'] = pd.to_datetime(df['date_time'])
df['hour'] = df['date_time'].dt.hour

def traffic_category(x):
    if x < 2000:
        return 'Low'
    elif x < 4000:
        return 'Medium'
    else:
        return 'High'

df['traffic_level'] = df['traffic_volume'].apply(traffic_category)

# UI Title
st.title("🚦 Traffic Pattern Analyzer")

st.write("Analyze traffic patterns based on time and weather")

# User Inputs
hour = st.slider("Select Hour", 0, 23, 10)
weather = st.selectbox("Select Weather", df['weather_main'].unique())

# Filter Data
filtered = df[(df['hour'] == hour) & (df['weather_main'] == weather)]

# Output
if st.button("Analyze Traffic"):
    if len(filtered) > 0:
        most_common = filtered['traffic_level'].mode()[0]
        st.success(f"Predicted Traffic Level: {most_common}")

        st.write("### Sample Data")
        st.dataframe(filtered.head())
    else:
        st.warning("No data available for selected conditions")

# Visualization
st.write("### Traffic Trend by Hour")

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.lineplot(x='hour', y='traffic_volume', data=df, ax=ax)
ax.set_title("Traffic Volume by Hour")

st.pyplot(fig)