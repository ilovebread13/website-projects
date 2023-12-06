import streamlit as st
from PIL import Image

st.set_page_config(page_title='General Mathematics', page_icon=':books:', layout='wide')

img_r_formula = Image.open('images/r_formula.png')
img_n_formula = Image.open('images/n_formula.png')
st.sidebar.success('Please select a page from above')

with st.container():
    st.title("General Mathematics: Future Value of General Annuity Calculator")
    st.write('---')
    st.subheader('This will be used to calculate the Future values for the performance task in General Mathematics')
    st.write('##')






