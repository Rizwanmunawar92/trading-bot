import streamlit as st

st.title("My First App")
st.write("Hello Rizwan!")

coin ="BTC"
price = 59000

if price == 60000:
    st.write("Perfect Entry:",price)
elif price < 60000:    
    st.write('BUY',coin,'at price',price)
elif price > 65000:
    st.write('Sell',coin,'at price', price)   
else:
    st.write('Wait - current price', price)


    

