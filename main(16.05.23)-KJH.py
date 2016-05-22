# -*- coding: utf-8 -*-

#import urllib

#url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml"

#data = urllib.request.urlopen(url).read()

#xmlFile = "test.xml"
#f = open(xmlFile, "wb")
#f.write(data)
#f.close()

import http.client

#conn = http.client.HTTPConnection("data.ex.co.kr")
#conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml")
#
#req = conn.getresponse()
#print(req.status, req.reason)
#
#cLen = req.getheader("Content-Length")
#req.read(cLen).decode("utf-8")


def getDataFromServiceArea(serviceArea):
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&serviceAreaName=" + str(serviceArea.encode('euc-kr')))
    
    req = conn.getresponse()
    print(req.status)  

#    cLen = req.getheader("Content-Length")
    if int(req.status) == 400 :
        return extractData(req.read().decode("utf-8"))
    pass

def extractData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    listElements = tree.getiterator("list")
    for list in listElements:
        serviceAreaName = list.find("serviceAreaName")
        menu = list.find("batchMenu")
        print(serviceAreaName)
        print (menu)
#        if len(menu.text) > 0 :
#            return {"serviceAreaName":serviceAreaName.text, "menu":menu.text}
    pass


serviceArea = str(input ('Service Area Name: '))
getDataFromServiceArea(serviceArea)