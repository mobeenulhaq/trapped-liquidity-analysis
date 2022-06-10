import ccxt
from datetime import datetime
import asyncio
import csv

from requests import head

now = datetime.now()

api_key = ''
api_key_secret = ''

exchange = ccxt.ftx({
    'enableRateLimit': True,  # required by the Manual https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
    'apiKey': api_key,
    'secret': api_key_secret,
    'options': {  # exchange-specific options
        'defaultType': 'future',  # switch to a futures API/account
    },
})

file_name = "btc-price-oi.csv"

# file appending function
async def price_oi_coroutine():
    with open(file_name, 'a', newline="") as f:
        writer = csv.writer(f)
        while True:
            now = datetime.now()
            await asyncio.sleep(60) # data needs to be plotted and analysed per 6o seconds
            price = exchange.fetch_ticker("BTC-PERP")['info']['price']
            oi = exchange.fetch_funding_rate(symbol = "BTC-PERP", params = {'datetime' : now})['info']['openInterest']
            writer.writerow([now, price, oi])

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(price_oi_coroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()