# -*- coding: utf-8 -*-

import http.client
from xml.dom.minidom import parse

conn = http.client.HTTPConnection("data.ex.co.kr")
conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=8YW8HGuC1ykwBMJNFG7HXG8WkModUbdksUy7Bstt2JRvPaziujIBzRBswk5I54TZORdz23ZL44iYwBWhZFuzYQ%3D%3D&type=xml")

req = conn.getresponse()
print(req.status, req.reason)
cLen = req.getheader("Content-Length")
req.read(cLen).decode("utf-8")

