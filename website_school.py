import streamlit as st

st.set_page_config(page_title='General Mathematics', page_icon=':books:', layout='wide')

with st.container():
    st.title("General Mathematics: Future Value of General Annuity Calculator")
    st.write('---')
    st.subheader('This will be used to calculate the Future values for the performance task in General Mathematics')
    st.write('##')


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

    return f"Your future value is: {round(future_value, 2)} Your P is: {round(P, 2)}"


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
    left_column, right_column = st.columns(2)
    with left_column:
        loan = st.text_input("Loan:")
        time_years = st.text_input("Time in years:")
        period_time = st.text_input("Period in time:")
        interest_rate = st.text_input("Interest rate:")
        nPP = st.text_input("nPP:")
    st.write('##')

    if st.button("Calculate Future value of General Annuity"):
        result = calculate_future_value(loan, time_years, period_time, interest_rate, nPP)
        st.write(result)
        result1 = r_n_location(interest_rate, period_time, nPP, time_years)
        st.write(result1)
