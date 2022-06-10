import ftxclient
from environs import Env

class Data:

    def __init__(self):
        env = Env()
        env.read_env()
        # set up ftx client
        self.ftx_client = ftxclient.FtxClient(
            api_key=env.str('FTX_KEY'), api_secret=env.str('FTX_SECRET'))

    def get_oi(self):
        # query FTX
        resp = self.ftx_client.get('/futures/BTC-PERP')['openInterest']
        return resp

    def get_price(self):
        # query FTX
        resp = self.ftx_client.get('/futures/BTC-PERP')['last']
        return resp
