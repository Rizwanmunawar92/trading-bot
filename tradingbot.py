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

price =st.number_input("Enter BTC Price", Value = 58000)

st.write(f"Price: {price} | Time: {time.ctime()}")

decision = trading_decision(price)
st.write (f"Decision: {decision}")

if st.button("Increase Price"):
    price +=200
    st.write(f"New Price: {price}")
    st.write(f" Decision: {decision}")
    

''' Day 2 Code for terminal use'''
'''import streamlit as st

st.title("My First App")
st.write("Hello Rizwan!")

import time

def trading_decision(price): #function refined
    if price == 60000: #rules for the function defined from line 9 - 16.
        print("Perfect Entry")
    elif price < 60000:
        print("BUY")
    elif price > 65000:
        print("SELL")
    else:
        print("WAIT")


price = 58000  # current price, in future I will try and learn to get this price from the real plateform 

# while loop current defined
while True:  
    print("Price:",price, "Time:", time.ctime()) # code added to print price with current time. 
    trading_decision(price)   # above define function called here.
    price +=200     #simulating price  but in future I will make it to track real time data/price/

    if price >=66000:     #loop break condition set 
        print("Stopping loop - target reached")
        break

    time.sleep(2)         # function called to run code every 2 seconds



        # Code add below is to practice use coin name and price in the defined funtion. '''
    
    
    '''import time
    def trading_decision(coin, price):
    print(f"{coin} price: {price}")
    if price == 60000:
        print("Perfect Entry")
    elif price < 60000:
        print("BUY")
    elif price > 65000:
        print("SELL")
    else:
        print("WAIT")

coin = "BTC"
price = 58000

while True:
    trading_decision(coin, price)

    price += 200  # simulate price

    if price >= 66000:
        print("Stopping loop - target reached")
        break

    print(f"Time: {time.ctime()}")
    time.sleep(2) '''
