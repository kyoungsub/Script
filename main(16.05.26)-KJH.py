# -*- coding: utf-8 -*-

#import urllib

#url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml"

#data = urllib.request.urlopen(url).read()

#xmlFile = "test.xml"
#f = open(xmlFile, "wb")
#f.write(data)
#f.close()

import http.client
import urllib

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
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&serviceAreaName=" +  str(urllib.parse.quote(serviceArea)))
    req = conn.getresponse()
    #req.add_header('User-Agent', User_Agent)
    
    if int(req.status) == 200 :
        print("검색 완료!")
        return extractData(req.read().decode("utf-8"))
    conn.close()
    pass

def extractData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    listElements = tree.getiterator("list")
    for list in listElements:
        direction = list.find("direction")
        serviceAreaName = list.find("serviceAreaName")
        menu = list.find("batchMenu")
        salePrice = list.find("salePrice")
        if len(menu.text) > 0 :
            print('===========================')
            print("방향:", direction.text)
            print("휴게소 이름:", serviceAreaName.text, "휴게소")
            print("가격:", salePrice.text)
            print ("메뉴:", menu.text)
            print('===========================')
#        if len(menu.text) > 0 :
#            return {"serviceAreaName":serviceAreaName.text, "menu":menu.text}
    pass


serviceArea = str(input ('Service Area Name: '))
getDataFromServiceArea(serviceArea)