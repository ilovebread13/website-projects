import streamlit as st



st.set_page_config(page_title='Homepage', page_icon=':books:', layout='wide')
st.sidebar.success('Please select a page from above')

with st.container():
    st.title('Home')
    st.write('---')
    st.subheader('Welcome to my website, for now it will only contain two pagese consisting of this and the calculator.')
    st.write('##')
    st.write('---')



with st.container():
    rain(
        emoji='❄',
        font_size=32,
        falling_speed=5,
        animation_length='infinite',
    )
