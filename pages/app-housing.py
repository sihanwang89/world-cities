import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Sihan Wang')

df = pd.read_csv('housing.csv')

# 1. slider: minimal median house value
value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)

st.subheader('See more filters in the sidebar:')

# 2. sidebar multiselect: location type (options taken from the full data)
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),   # options
    df.ocean_proximity.unique())   # defaults: all selected

# 3. sidebar radio: income level
income_level = st.sidebar.radio('Choose income level', ['Low', 'Medium', 'High'])

# filter by median house value
df = df[df.median_house_value >= value_filter]

# filter by location type
df = df[df.ocean_proximity.isin(location_filter)]

# filter by income level
if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_level == 'High':
    df = df[df.median_income >= 4.5]

# 4. map of the filtered districts
st.map(df)

# 5. histogram of median house value below the map
fig, ax = plt.subplots(figsize=(20, 5))
ax.hist(df['median_house_value'], bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Number of Districts')
st.pyplot(fig)
