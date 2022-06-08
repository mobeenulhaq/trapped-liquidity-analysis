import ccxt
from datetime import datetime
import asyncio

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

# fetching ticker price
async def price_coroutine():
    while True:
        now = datetime.now()
        await asyncio.sleep(60) # data needs to be plotted and analysed per 6o seconds
        price = exchange.fetch_ticker("BTC-PERP")['info']['price']
        print(price, now)

# fetching ticker open interest
async def oi_coroutine():
    while True:
        now = datetime.now()
        await asyncio.sleep(60)
        oi = exchange.fetch_funding_rate(symbol = "BTC-PERP", params = {'datetime' : now})['info']['openInterest']
        print(oi, now)

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(price_coroutine())
    asyncio.ensure_future(oi_coroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()