import streamlit as st

st.title("My First App")
st.write("Hello Rizwan!")

import time

coin = "BTC"
price = 65000

while True:
    print("price :",price,time.ctime()) # time.ctime used to print readable time on the terminal
    
    if price < 60000:
        print("Buy", price)
    elif price > 65000:
        print("SELL:",price)
    else:
        print("WAIT")

    price += 200 #will simulate price

    if price >= 66000:
        print("Stopping loop - Target reached")
        break


    time.sleep(2)

    

