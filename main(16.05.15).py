# -*- coding: utf-8 -*-

import urllib

url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml"

data = urllib.request.urlopen(url).read()

xmlFile = "test.xml"
f = open(xmlFile, "wb")
f.write(data)
