''' Day 2 Code Stream lit version'''

import streamlit as st

st.title("My Frist App ")
st.write("Welcome Rizwan")

import time

def trading_decision(price): 
    if price == 60000:
        return "Perfect Entry"
    elif price < 60000:
        return "BUY"
    elif price > 65000:
        return "SELL"
    else:
        return "WAIT"

price =st.number_input("Enter BTC Price", value = 58000)

st.write(f"Price: {price} | Time: {time.ctime()}")

decision = trading_decision(price)
st.write (f"Decision: {decision}")

if st.button("Increase Price"):
    price +=200
    st.write(f"New Price: {price}")
    st.write(f" Decision: {decision}")
