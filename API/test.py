import pprint
import time
import requests
import json

from ambient_api.ambientapi import AmbientAPI

weather = AmbientAPI(log_level='CONSOLE')
response = requests.get('https://rt.ambientweather.net/v1/devices/')
data = response.json()


def test_endpoint():
    assert weather.endpoint == 'https://rt.ambientweather.net/v1'


devices = weather.get_devices()


def test_devices():
    assert len(devices) == 0

if isinstance(data, list) and len(data) > 0:
    # Take the first item to show keys
    first_item = data[0]
    print("Parameter names (keys) in the JSON response:")
    for key in first_item.keys():
        print(f"* {key}")
elif isinstance(data, dict):
    print("Parameter names (keys) in the JSON response:")
    for key in data.keys():
        print(f"* {key}")
else:
    print("JSON response is not a dictionary or list of dictionaries.")
for device in devices:
    # Wait two seconds between requests so we don't get a 429 response.
    # https://ambientweather.docs.apiary.io/#introduction/rate-limiting
    # This probably won't happen much in real world situations.
    time.sleep(2)
    
    
    #response = requests.get('https://rt.ambientweather.net/v1/devices')
    #response.raise_for_status()
    
    #data = response.json()
    #json_str = json.dumps(data)
    #resp = json.loads(json_str)
    #print(resp)
    #print(json.dumps(data, indent=4))
    
    
    
    
    
    
    
    
    print('Device')
    print((str(device)))
    
    #call all data
    devicedata = (device.last_data)
    #identify top-level param
    winddir = (devicedata['winddir'])

    #display param responses
    #print(winddir)
    if winddir >0 and winddir <90:
            print("NE")
    #print('           2.5 Oz is $',round((1/silver)*2.5, 2))
    #print('             5 Oz is $',round((1/silver)*5, 2))
    

    #print('Last Data')
    #pprint.pprint(device.last_data)

    #print('Get Data')
    #pprint.pprint(device.get_data())
