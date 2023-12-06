import streamlit as st


st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')
st.sidebar.success('Please select a page from above')

with st.container():
    st.title("Home")
    st.write('---')
    st.subheader('Welcome to my website, for now it will only contain two pages consisting of this and the calculator. It will eventually increase in the future.')
    st.write('##')
    st.write('---')

with st.container():
    st.subheader('Contents')
    st.write('---')





