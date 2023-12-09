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
img_future = Image.open('images/future.png')
img_pvci = Image.open('images/pvci.png')


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


def calculate_option1(down_payment, future_value, interest_rate, time_years):
    try:
        down_payment = float(down_payment)
        future_value = float(future_value)
        interest_rate = float(interest_rate)
        time_years = float(time_years)
    except ValueError:
        return 'Invalid input. Please enter numerical values.'

    PV = (future_value / ((1 + interest_rate) ** time_years))
    EV = PV + down_payment
    return (f'For option 1, your economic value is: ₱ {round(EV, 2)} '
            f'Your present value is: ₱ {round(PV, 2)}')


def calculate_option2(down_payment, periodic_payment, interest_rate, time_years, compounding_period, nPP):
    try:
        down_payment = float(down_payment)
        periodic_payment = float(periodic_payment)
        interest_rate = float(interest_rate)
        time_years = float(time_years)
        compounding_period = float(compounding_period)
        nPP = float(nPP)
    except ValueError:
        return 'Invalid input. Please enter numerical values.'

    n = time_years * nPP
    r = (1 + (interest_rate / compounding_period)) ** (compounding_period / nPP) - 1
    PV = periodic_payment * ((1 - ((1 + r) ** (-n))) / r)
    EV = PV + down_payment
    return (f'For option 2, your economic value is: ₱ {round(EV, 2)}, '
            f'Your present value is: ₱ {round(PV, 2)}, '
            f'Your r is: {r}')

def calculate_pvdef(periodic_payment, deferred_periods, interest_rate, compounding_period, time_years, payment):
    try:
        periodic_payment = float(periodic_payment)
        deferred_periods = float(deferred_periods)
        interest_rate = float(interest_rate)
        compounding_period = float(compounding_period)
        time_years = float(time_years)
        payment = float(payment)

        if payment == 1:
            D = deferred_periods * compounding_period - payment
        elif payment <= 0:
            D = deferred_periods * compounding_period
        elif payment > 1:
            D = deferred_periods * compounding_period

    except ValueError:
        return 'Invalid input. Please enter numerical values.'
    r = interest_rate / compounding_period
    p = compounding_period * time_years
    PV_def = periodic_payment * ((((1 + r) ** (-deferred_periods)) - ((1 + r) ** -(p + deferred_periods))) / r)
    return (f'Your present value deferred annuity is: ₱ {round(PV_def, 2)} Your D is: {D} '
            f'Your r is: {r} ' f'Your p is: {p}')


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
st.subheader('A calculator for getting the present value of deferred annuity')
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        periodic_payment = st.text_input('Periodic payment (R): ')
        deferred_periods = st.text_input('Number of deferred periods (D): ')
        interest_rate = st.text_input('Interest rate (I): ')
        compounding_period = st.text_input('Compounding period (M): ')
        time_years = st.text_input('Time in years (T): ')
        payment = st.text_input('Did the person pay? put 1, if not, put 0: ')
    with col2:
        st.write('##')
        st.image(img_pvdef)
        st.write('##')
        st.image(img_rate_formula)
        st.write('##')
        st.image(img_tnopp)
        st.write('##')

    if st.button('Calculate Present value of deferred annuity'):
        result = calculate_pvdef(periodic_payment, deferred_periods, interest_rate, compounding_period, time_years,
                                 payment)
        st.write(result)





st.write('---')
st.subheader('|LIMITED| A calculator made for getting the answers/values for the option 1 and option 2 in fair market value.')
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        down_payment = st.text_input('Down payment (DP) : ')
        future_value = st.text_input('Future value (FV): ')
        interest_rate = st.text_input('Interest rate (i): ')
        time_years = st.text_input('Time in years (t): ')
        periodic_payment = st.text_input('Periodic payment (P): ')
        compounding_period = st.text_input('Compounding period (m): ')
        nPP = st.text_input('No. of payments (nPP):')
    with col2:
        st.write('##')
        st.image(img_pvci)

    if st.button('Calculate the value for the present value of compound interest, option 1'):
        result = calculate_option1(down_payment, future_value, interest_rate, time_years)
        st.write(result)
    if st.button('Calculate the value for the option 2'):
        result1 = calculate_option2(down_payment, periodic_payment, interest_rate, time_years, compounding_period, nPP)
        st.write(result1)


st.write('---')
switch_pages = st.button('Go back to homepage')
if switch_pages:
    switch_page('homepage')
st.write('##')




