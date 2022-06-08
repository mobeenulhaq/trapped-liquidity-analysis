import time
import hmac
from requests import Request

api_key = 'dseus8OVcqRSM9U76c1C6HAr_9nrpB5mNx5A9EC0'
api_key_secret = 'mc84pfXhfnDyXIw6-_cEzq2mNGsHv8QvK4q_SWk_'
endpoint = 'https://ftx.com/api/'

ts = int(time.time() * 1000)
request = Request('GET', endpoint)
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new(api_key_secret.encode(), signature_payload, 'sha256').hexdigest()

prepared.headers['FTX-KEY'] = api_key
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)
