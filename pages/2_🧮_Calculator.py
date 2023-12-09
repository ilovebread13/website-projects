import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='General Mathematics', page_icon=':books:', layout='wide')

img_r_formula = Image.open('images/r_formula.png')
img_n_formula = Image.open('images/n_formula.png')
img_pvdef = Image.open('images/pvdef.PNG')
img_rate_formula = Image.open('images/rate.PNG')
img_tnopp = Image.open('images/tnopp.PNG')




st.sidebar.title('🏫 11-Palladium')
st.sidebar.caption('Check out the current pages here')
st.sidebar.markdown('Made by a student ❤')
st.sidebar.markdown('---')
st.sidebar.success('Please select a page from above')
st.sidebar.write('---\n')
st.sidebar.caption('''If you want to check the source code, [here](https://github.com/ilovebread13/website-projects)''')
st.sidebar.write('---\n')

with st.container():
    rain(
        emoji='❄',
        font_size=16,
        falling_speed=5,
        animation_length='infinite',
    )

with st.container():
    st.title("General Mathematics: Future Value of General Annuity Calculator")
    st.write('---')
    st.subheader('This will be used to calculate the Future values for the performance task in General Mathematics')


def calculate_future_value(loan, time_years, period_time, interest_rate, nPP):
    try:
        loan = float(loan)
        time_years = float(time_years)
        period_time = float(period_time)
        interest_rate = float(interest_rate)
        nPP = float(nPP)
    except ValueError:
        return "Invalid input. Please enter numerical values."

    n = time_years * nPP
    r = (1 + (interest_rate / period_time)) ** (period_time / nPP) - 1
    P = loan / ((1 - (1 + r) ** (-n)) / r)
    future_value = P * ((((1 + r) ** n) - 1) / r)

    return f"Your future value is: ₱ {round(future_value, 2)} Your P is: ₱ {round(P, 2)}"


def calculate_interest(loan, time_years, period_time, interest_rate, nPP):
    try:
        loan = float(loan)
        time_years = float(time_years)
        period_time = float(period_time)
        interest_rate = float(interest_rate)
        nPP = float(nPP)
    except ValueError:
        return ""

    n = time_years * nPP
    r = (1 + (interest_rate / period_time)) ** (period_time / nPP) - 1
    P = loan / ((1 - (1 + r) ** (-n)) / r)
    future_value = P * ((((1 + r) ** n) - 1) / r)
    interest = future_value - loan
    return f"Your interest is: ₱ {round(interest, 2)}"


def r_n_location(interest_rate, period_time, nPP, time_years):
    try:
        time_years = float(time_years)
        period_time = float(period_time)
        interest_rate = float(interest_rate)
        nPP = float(nPP)

    except ValueError:
        return ""

    r = (1 + (interest_rate / period_time)) ** (period_time / nPP) - 1
    n = n = time_years * nPP

    return f"Your r is: {r} Your n is: {n}"


with st.container():
    left_column, right_column = st.columns((2, 1))
    with left_column:
        loan = st.text_input("Loan:")
        time_years = st.text_input("Time in years:")
        period_time = st.text_input("Period in time:")
        interest_rate = st.text_input("Interest rate:")
        nPP = st.text_input("nPP:")
    st.write('##')

    with right_column:
        st.write('##')
        st.image(img_r_formula)
        st.write('##')
        st.image(img_n_formula)

    if st.button("Calculate Future value of General Annuity"):
        result = calculate_future_value(loan, time_years, period_time, interest_rate, nPP)
        st.write(result)
        result1 = r_n_location(interest_rate, period_time, nPP, time_years)
        st.write(result1)
        result2 = calculate_interest(loan, time_years, period_time, interest_rate, nPP)
        st.write(result2)

st.write('---')
st.subheader('This will be the calculator for the performance task in General Mathematics as well. Use this for checking the answers and values')
switch_pages = st.button('Go back to homepage')
with st.container:
    col1, col2 = st.columns((2, 1))
    with col1:
        st.text_input('Periodic payment (R): ')
        st.text_input('Number of deferred periods (D): ')
        st.text_input('Interest rate (I): ')
        st.text_input('Compounding period (M): ')
        st.text_input('Time in years (T): ')
        st.text_input('Did the person pay? Y/N, if not, leave blank: ')
    with col2:
        st.write('##')
        st.image(img_pvdef)
        st.write('##')
        st.image(img_rate_formula)
        st.write('##')
        st.image(img_tnopp)
        st.write('##')



if switch_pages:
    switch_page('homepage')
st.write('##')




