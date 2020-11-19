import hashlib, requests, hmac, json
import urllib
import os

API_KEY = os.environ.get('binance_api')
SECRET_KEY = os.environ.get('binance_secret')
END_POINT = 'https://testnet.binance.vision/api/v3'


def delete_order(orderId):
	api_method = '/order'
	time = requests.get(END_POINT + '/time')
	serverTime = json.loads(time.text)['serverTime']
	param = {'symbol':'LTCBTC', 'orderId':orderId, 'timestamp':serverTime}
	hashedsig = generate_signature(param)
	param['signature'] = hashedsig
	userdata = requests.delete(END_POINT + api_method, params = param, headers = {"X-MBX-APIKEY" : API_KEY,})

	print(userdata.text)

def order():
	api_method = '/order'
	time = requests.get(END_POINT + '/time')
	serverTime = json.loads(time.text)['serverTime']
	param = {'symbol':'LTCBTC',
			'side':'BUY',
			'type':'LIMIT',
			'timeInForce' : 'GTC',
			'price' : 0.01,
			'quantity': 1,
			'timestamp': serverTime}
	hashedsig = generate_signature(param)
	param['signature'] = hashedsig
	userdata = requests.post(END_POINT + api_method, params = param, headers = {"X-MBX-APIKEY" : API_KEY,})

	print(userdata.text)

def generate_signature(param):
	p = urllib.parse.urlencode(param)
	hashedsig = hmac.new(SECRET_KEY.encode('utf-8'), p.encode('utf-8'), hashlib.sha256).hexdigest()
	return hashedsig


if __name__ == '__main__':
	while True:
		try:
			option = int(input('''please select an action
			1. order
			2. delete
			3. exit\n'''))

			if option < 1 or option > 3:
				print('Invalid option!')
				continue
			elif option == 1:
				order()
			elif option == 2:
				orderId = int(input('Enter order ID to delete: '))
				delete_order(orderId)
			else:
				break

		
		except ValueError as e:
			print('Invalid option!')
			print(e)

   