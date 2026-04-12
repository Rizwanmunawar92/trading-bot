import time

def trading_decision(price):
    if price == 60000:
        return "PERFECT ENTRY"
    elif price < 60000:
        return "BUY"
    elif price > 65000:
        return "SELL"

    else:
        return "WAIT"

# take input from user
price=float(input("Enter BTC Price:"))

while True:
    print (f"BTC Price:{price} | TIME: {time.ctime()}")
    decision = trading_decision(price)
    print(f"Decision: {decision}")

    price += 300

    if price >= 67000:
        print("Stopping loop - Target reached")
        break

    time.sleep(2)