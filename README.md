# LoRa-weather
This is a project to facilitate sharing live weather information via Meshtastic

The API calls are designed for the Ambient Weather Network ambient_api. If you use a different API you will need to adjust certain parameters. This ReadMe is being written before the LoRa / weather integration so those parameters are not yet defined. I will update this ReadMe with more info as I progress

I am not a terribly skilled coder. This is a combination of Google, YouTube, ChatGPT, and putzing around so I make no guarantees that the code will work on your machine, or that it will even be safe to run on your machine. Prototyping is being done in Thonny on a Raspberry Pi 400

TO GET STARTED
1. Open API/ambient_api/settings.py
2. Add your API Key and Application Key
3. Run API/ambient_api/test.py. This should return actual values from your station. If it does not, there is something wrong with your keys
4. After getting test.py to run correctly, try running API/ambient_api/UserInput.py
    i. Modify the parameters to return what you actually want to see
   ii. Modify the print() values so that the user-friendly text is relevant to your use-case
