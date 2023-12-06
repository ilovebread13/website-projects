import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')
st.sidebar.success('Please select a page from above')

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
        label='Contents',
        color_name='violet-70',
        description=''
    )
    def calculator():
    switch_pages = st.button('Go to Calculator!')
    if switch_pages:
        switch_page('2_🧮_Calculator.py')

    

