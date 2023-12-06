import streamlit as st
from streamlit_extras.colored_header import colored_header


st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')
st.sidebar.success('Please select a page from above')

with st.container():
    st.title('Home')
    st.write('---')
    st.subheader('Welcome to my website, for now it will only contain two pagese consisting of this and the calculator.')
    st.write('##')
    st.write('---')

colored_header(
    label='Contents',
    color_name='violet-70'
)
import streamlit as st
from streamlit_extras.colored_header import colored_header


st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')
st.sidebar.success('Please select a page from above')

with st.container():
    st.title('Home')
    st.write('---')
    st.subheader('Welcome to my website, for now it will only contain two pagese consisting of this and the calculator.')
    st.write('##')
    st.write('---')

colored_header(
    label='Contents',
    color_name='violet-70'
)
