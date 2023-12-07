import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')

st.sidebar.title('🏫 11-Palladium')
st.sidebar.caption('Check out the current pages here')
st.sidebar.markdown('Made by a student ❤')
st.sidebar.markdown('---')

img_homepage = Image.open('images/homepage.png')

with st.container():
    rain(
        emoji='❄',
        font_size=16,
        falling_speed=5,
        animation_length='infinite',
    )

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1 = st.write('##')
    with col2 = st.image(img_homepage)
    with col3 = st.write('##')
    
    st.write('---')
    st.write('##')
    st.markdown("<h2 style='text-align: center; color: white; font_size: 10px;'> Welcome to our website! </h2>", unsafe_allow_html=True)
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
    st.write('##')
    switch_pages1 = st.button('2. Go to rocks section!')
    if switch_pages1:
        switch_page('rocks')

st.sidebar.success('Please select a page from above')
st.sidebar.write('---\n')
st.sidebar.caption('''If you want to check the source code, [here](https://github.com/ilovebread13/website-projects)''')
st.sidebar.write('---\n')
    

