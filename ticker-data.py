import ccxt

api_key = 'BqFWu1dFEidOphVrx6yCGTycDAlAdTWEXhWKUXkJ'
api_key_secret = 'v8EJw2iVA3b3RFEKFfcUPlpSZiYvtkrImUPe4bX0'

exchange = ccxt.ftx({
    'enableRateLimit': True,  # required by the Manual https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
    'apiKey': api_key,
    'secret': api_key_secret,
    'options': {  # exchange-specific options
        'defaultType': 'future',  # switch to a futures API/account
    },
})

# print(dir(publicGetFuturesFutureNameStats))
#print(exchange.fetch_funding_rate(symbol ='BTC-PERP', params = {'datetime' : '2022-01-05T16:00:00+00:00'}))

ticker = input("Enter ticker: ")
ticker = ticker.upper() + "-PERP"

oi = exchange.fetch_funding_rate(symbol = ticker, params = {'datetime' : '2022-01-05T16:00:00+00:00'})['info']['openInterest']
