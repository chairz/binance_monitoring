# Introduction

This project is written using Python3 and tested on macOS environment. There are 2 files in this project `user_stream.py` and `user_action.py`. 

`user_stream.py` is a web socket listener that will log `executionReport` event and checks if the **delay** between `Event Time` and current time is greater than the user-preset threshold. 

`user_action.py` has 2 functionality: ordering and deleting orders. By selecting ordering, a dummy order will be sent by default as follows:
  {'symbol':'LTCBTC',
  'side':'BUY',
  'type':'LIMIT',
  'timeInForce' : 'GTC',
  'price' : 0.01,
  'quantity': 1,
  'timestamp': serverTime}.
  Deleting an order requires an orderId field which can be obtained after completing an order.
  
  # Setting Up
  There may be some python dependencies package that requires installation. The missing packages will be prompt to you when executing the python file which can be installed using the python package manager `pip3 install <missing package>`
  The programs retrieve the **api key** and **secret key** through environment variables. Export the keys to `binance_api` and `binance_secret` respectively. 
  
  `export binance_api=<your api key>`
  
  `export binance_secret=<your secret key>`
  
  
  # Running
  Launch a terminal and execute `python3 user_stream.py`. The program will request for a delay threshold and if the connection to socket is successful, the program will prompt the message: `listening for events...`. Open another terminal and execute `python3 user_action.py` to simulate user actions to test the alert function of the web socket listener.
  
![Alt text](https://github.com/chairz/binance_monitoring/blob/main/img/demo.png?raw=true "Demo Alert")
