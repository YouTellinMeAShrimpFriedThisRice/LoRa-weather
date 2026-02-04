import os

try:
    AMBIENT_ENDPOINT = "https://rt.ambientweather.net/v1"
  # For both keys below, replace the less than/greater than symbols and the text between them with the actual key. The key should be nested inside single quotes and then inside parenthesis 
    AMBIENT_APPLICATION_KEY = str('<YOUR APPLICATION KEY HERE>')
    AMBIENT_API_KEY = str('<YOUR API KEY HERE>')
except KeyError:
    pass
