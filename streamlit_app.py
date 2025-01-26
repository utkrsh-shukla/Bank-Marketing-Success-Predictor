import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the dashboard
st.title("Bank Marketing Campaign Analysis Dashboard")

# Load the dataset
@st.cache_data  # Cache the data to improve performance
def load_data():
    return pd.read_csv("train.csv")

df = load_data()

# Display the dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Sidebar for filters
st.sidebar.header("Filters")
selected_job = st.sidebar.selectbox("Select Job", df['job'].unique())
selected_education = st.sidebar.selectbox("Select Education", df['education'].unique())
selected_marital = st.sidebar.selectbox("Select Marital Status", df['marital'].unique())

# Filter the dataset based on user selection
filtered_df = df[
    (df['job'] == selected_job) &
    (df['education'] == selected_education) &
    (df['marital'] == selected_marital)
]

# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_df)

# Visualizations
st.subheader("Key Insights")

# 1. Target Variable Distribution
st.write("### Subscription Rate (Target Variable)")
fig, ax = plt.subplots()
sns.countplot(x='target', data=filtered_df, ax=ax)
ax.set_title("Distribution of Subscriptions (Yes/No)")
st.pyplot(fig)

# 2. Age Distribution by Subscription
st.write("### Age Distribution by Subscription")
fig, ax = plt.subplots()
sns.histplot(data=filtered_df, x='age', hue='target', kde=True, ax=ax)
ax.set_title("Age Distribution by Subscription")
st.pyplot(fig)

# 3. Balance Distribution by Subscription
st.write("### Balance Distribution by Subscription")
fig, ax = plt.subplots()
sns.histplot(data=filtered_df, x='balance', hue='target', kde=True, ax=ax)
ax.set_title("Balance Distribution by Subscription")
st.pyplot(fig)

# 4. Duration vs Subscription
st.write("### Call Duration vs Subscription")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x='target', y='duration', ax=ax)
ax.set_title("Call Duration vs Subscription")
st.pyplot(fig)

# 5. Campaign Contacts vs Subscription
st.write("### Number of Contacts vs Subscription")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x='target', y='campaign', ax=ax)
ax.set_title("Number of Contacts vs Subscription")
st.pyplot(fig)

# 6. Previous Campaign Outcome vs Subscription
st.write("### Previous Campaign Outcome vs Subscription")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='poutcome', hue='target', ax=ax)
ax.set_title("Previous Campaign Outcome vs Subscription")
st.pyplot(fig)

# 7. Correlation Heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation Heatmap")
st.pyplot(fig)
