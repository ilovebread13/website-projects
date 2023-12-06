import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

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
    col1, col2, col3 = st.columns(3)
    st.subheader('🏠 Home')
    st.write('---')
    st.write('##')
    with col1:
        st.write('')
    with col2:
        st.subheader('Welcome to my website, for now it will only contain two pages consisting of this and the calculator.')
    with col3:
        st.write('')
    st.write('##')
    st.write('---')

with st.container():
    colored_header(
        label='Contents',
        color_name='violet-70',
    )


