import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page


st.sidebar.title('🏫 11-Palladium')
st.sidebar.caption('Check out the current pages here')
st.sidebar.markdown('Made by a student ❤')
st.sidebar.markdown('---')
st.sidebar.success('Please select a page from above')
st.sidebar.write('---\n')
st.sidebar.caption('''If you want to check the source code, [here](https://github.com/ilovebread13/website-projects)''')
st.sidebar.write('---\n')

img_rocks = Image.open('images/rocks.png')


with st.container():
  st.title('15 interesting rocks from National Geographic')

with st.container():
  col1, col2, col3 = st.columns(3)
  with col1:
    st.write('##')
  with col2: 
    st.image(img_rocks)
  with col3:
    st.write('##')
  switch_pages = st.button('Go back to homepage')
  if switch_pages:
    switch_page('homepage')
