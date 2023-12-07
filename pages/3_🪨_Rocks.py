import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page


img_rocks = Image.open('images/rocks.png/')

with st.container():
  col1, col2, col3 = st.columns(3)
  col1 = st.write('##')
  col2 = st.image(img_rocks)
  col3 = st.write('##')
