#import re

from test import data

responsetable = {
    "help": "You can make one request per message. Valid requests are Temp, Wind, Precip, or Forecast",
    "temp": "Current temp in Druid Hills is temptemptemp",
    "wind": "Current wind conditions are windwindwind",
    "precip": "It is currently rainingsnowingsleeting",
    "forecast": "The forecast is forecastforecastforecast"
    }


prompt = input('What would you like to know? Type Help for a list of options').lower().strip()


result = responsetable.get(prompt, "Invalid input. Please try again again again")
print(result)

prompt = ''

prompt = input('What would you like to know?').lower().strip()

result2 = responsetable.get(prompt, 'Invalid input')
print(result2,'. Thank you for your request. Please reconnect for additional inquiries')

#f re.search(help, prompt, re.IGNORECASE):
#    print('you can make one request per message. valid requests are:')

#if help.lower in input.lower:
 #   print(helprequest)
  #  if 'wind' in input:
   #     print(wind)
    #    if 'temp' in input:
     #       print(temp)