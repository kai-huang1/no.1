import json

import requests

r = requests.get("http://www.baidu.com",timeout=1)
s = r.text
st = "//www."
en = ".png"
n = s.find(st)
f = s.find(en)
print(s[n:f + len(en)])
b = r.elapsed.total_seconds()
print(r.elapsed.total_seconds())

assert "//www.baidu.com/img/bd_logo1.png" in r.text










