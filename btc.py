import requests

# Hacemos una petición GET a la API de Coinbase
response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')

# Obtenemos el precio de Bitcoin en USD
price = response.json()['data']['amount']

# Imprimimos el precio
print(f"El precio actual de Bitcoin es {price} USD")
