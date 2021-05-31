#!/usr/bin/python3
import requests

x = "http://158.69.76.135/level1.php/"
for i in range(4096):
    ho = requests.get(x)
    cookies = ho.cookies
    dictionary = cookies.get_dict()
    key = dictionary.get('HoldTheDoor')
    payload = {'id': '2806', 'key': key, 'holdthedoor': 'Enviar'}
    res = requests.post(x, data = payload, cookies = cookies)
    print("Vote n*{:d} Code:{} Key:{}".format(i, res, key))
