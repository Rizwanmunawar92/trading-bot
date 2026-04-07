import streamlit as st

st.title("My First App")
st.write("Hello Rizwan!")

coin ="BTC"
price = 65000

if price == 60000:
    print('Perfect Entry')
elif price < 60000:    
    print('BUY',coin,'at price',price)
elif price > 65000:
    print('Sell',coin,'at price', price)   
else:
    print('Wait - current price', price)


    

