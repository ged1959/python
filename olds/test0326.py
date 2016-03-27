# coding: utf-8
# 「超」入門。p.34

import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/jsion/v1';
payload = {"city":"130010"}
weather_data = requests.get(api_url, params=payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + 'の天気は、' + weather_data['forecasts'][0]['telop'])