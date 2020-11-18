import requests, json
import hashlib, hmac
import websockets, asyncio
import datetime
import os

API_KEY = os.environ.get('binance_api')
SECRET_KEY = os.environ.get('binance_secret')
END_POINT = 'https://testnet.binance.vision/api/v3'
STREAM_END_POINT = 'wss://testnet.binance.vision/ws/'


def setup():
	while True:
		try:
			max_delay_ms = int(input('please input max delay tolerance in milliseconds:'))
			break;
		except ValueError:
			print('Please input a valid integer')
	listenkey_json = requests.post(END_POINT + "/userDataStream",headers = {"X-MBX-APIKEY" : API_KEY,})
	listenkey = json.loads(listenkey_json.text)['listenKey']

	start_socket(listenkey, max_delay_ms)

def start_socket(listenkey, max_delay_ms):
	url = STREAM_END_POINT + listenkey
	print('listening for events...')
	async def _listen_for_events():
		while True:
			async with websockets.connect(url) as socket:
				event = await socket.recv()
				event_dict = json.loads(event)
				event_type = event_dict['e']
				if event_type == 'executionReport':
					event_time = event_dict['E']
					print('{},{}'.format(event_type, event_time))
					now = round(datetime.datetime.now().timestamp() * 1000)
					print(now)
					diff = now -event_time
					print(diff)
					if diff >= max_delay_ms:
						print("ALERT! DELAY {}ms IS GREATER THAN THRESHOLD OF {}ms".format(diff, max_delay_ms))
	asyncio.get_event_loop().run_until_complete(_listen_for_events())

if __name__ == '__main__':
    setup()