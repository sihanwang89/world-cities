import streamlit as st

st.set_page_config(page_title='World Cities', page_icon='\U0001F30D', layout='wide')

st.title('World Cities')

st.write("""
Welcome to the **World Cities** app!

This app helps you explore cities around the world with a population over one million.
You can filter cities by population size, capital type, and country, then see them
on a map, in a table, and as a bar chart of total population by country.

Use the button below to open the Cities Explorer.
""")

if st.button('Go to the Cities Explorer'):
    st.switch_page('pages/app.py')
