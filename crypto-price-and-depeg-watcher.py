import requests
import time
import sys

BASE_URL = "https://api.binance.com/api/v3/ticker/price"  #All pairs on binance will be displayed once this url is pasted to a browser

def get_price(symbol):
    url = f"{BASE_URL}?symbol={symbol}"
    visit_the_url = requests.get(url)  
    data = visit_the_url.json()              #. json() turns that text into a Python object
    return float(data["price"])

Stable_coins = ["USDCUSDT", "FDUSDUSDT", "TUSDUSDT"]
Target_price = 1.0
Range = 0.01   #1% means 0.99 to 1.01
Check_every = 60 #seconds

def watch_depeg():
    while True:
        print("---Checking---")
        for symbol in Stable_coins:
            price = get_price(symbol)
            lower_end = Target_price - Range
            upper_end = Target_price + Range

            if price < lower_end or price > upper_end:
                print(f"ALERT: {symbol} depegged, price = {price:.6f}")
            else:
                print(f"OK: {symbol} = {price:.6f}")

        time.sleep(Check_every)  # Pause for 60 seconds before checking again

if __name__ == "__main__":
    if len(sys.argv) > 1:   #sys is system      #argv is argument
        symbol = sys.argv [1].upper()   #All symbols are upper case so this makes sure everything sticks to that requirement
        
        if symbol == "WATCH": # the watch mode, so if you keep your VS code open it will run forever and warn whenever a stable coin depegs
            watch_depeg()
        else: 
            print(f"{get_price(symbol):.6f}")
    else:
        print("Give a symbol. For example, python depeg_watcher.py DOTUSDT")