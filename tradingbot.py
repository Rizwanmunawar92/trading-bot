import streamlit as st

st.title("My First App")
st.write("Hello Rizwan!")

import time

coin = "BTC"
price= 65000

while True:
    print("Price:",price)

    if price > 65000:
        print("SELL")
    elif price <60000:
        print("BUY")
    else:
        print("WAIT")

    price = price - 100 #simulate price change
    time.sleep(2)
    

