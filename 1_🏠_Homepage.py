import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')

st.sidebar.title('🏫 11-Palladium')
st.sidebar.caption('Check out the current pages here')
st.sidebar.markdown('Made by a student')

with st.container():
    rain(
        emoji='❄',
        font_size=16,
        falling_speed=5,
        animation_length='infinite',
    )

with st.container():
    
    st.subheader('🏠 Home')
    st.write('---')
    st.write('##')
    st.markdown("<h2 style='text-align: center; color: white; font_size: 10px;'> Welcome to my website, for now, it will only contain two pages consisting of this and the calculator. </h2>", unsafe_allow_html=True)
    st.write('##')
    st.write('---')

with st.container():
    colored_header(
        label='Contents:',
        color_name='violet-70',
        description=''
    )
    st.write('##')
    switch_pages = st.button('1. Go to Calculator!')
    if switch_pages:
        switch_page('calculator')

st.sidebar.success('Please select a page from above')
st.sidebar.write('---\n')
st.sidebar.caption('If you want to check the source code, [here](https://github.com/ilovebread13/website-projects')
st.sidebar.write('---\n')
    

