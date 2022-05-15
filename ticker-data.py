import ccxt

ftx = ccxt.ftx()

markets = ftx.load_markets()

print(markets.keys())