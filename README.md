# crypto-price-and-depeg-watcher
A small and naive command-line tool that checks any Binance pair and monitors stablecoins for depegs

# Features
* Get real-time price for any symbol from Binance API
* Depeg alert printed if price leaves the safe range
* “WATCH” mode to monitor stablecoins continuously (USDC, FDUSD, TUSD)
* The program automatically converts input into uppercase so everything works fine

# Instructions

## Live Price Checking
Copy and paste into the console:<br><br>
`python depeg_watcher.py BTCUSDT`<br><br>
The program will then retrieve the current price from Binance API and print in the console<br><br>
The pair can be the user's choice. For example XRPUSDT, TRXUSDT, DOTUSDT, etc <br><br>

## Stablecoin Depegs Watch
Copy and paste into the console:<br><br>
`python depeg_watcher.py watch`<br><br>
The program will then retrieve the current price of the stable coins from Binance API and print a warning should they depeg, the program will continue to check every 60 seconds unless the user interrupt the loop<br><br>

# Requirements
Users should first install the following before continuing<br><br>
`pip install requests`






