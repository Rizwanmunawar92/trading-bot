coin ="BTC"
price = 61000

if price < 60000:
    print('BUY',coin,'at price',price)
elif price > 65000:
    print('Sell',coin,'at price', price)
elif price == 60000:
    print('Perfect Entry')
else:
    print('Wait - current price', price)

    

