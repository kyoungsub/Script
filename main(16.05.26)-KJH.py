# -*- coding: utf-8 -*-

#import urllib

import http.client
import urllib

#global
loopflag = 1


#========================== 휴게소명 검색 ======================================
def getDataFromServiceArea(serviceArea):
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&serviceAreaName="
    +  str(urllib.parse.quote(serviceArea)))
    req = conn.getresponse()
    #req.add_header('User-Agent', User_Agent)
    
    if int(req.status) == 200 :
        print("\n 검색 완료!")
        return extractArea(req.read().decode("utf-8"))
    conn.close()
    pass

def extractArea(strXml):
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
#==============================================================================

#============================ 경로 검색 ========================================
def getDataFromRouteName(route):
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&routeName="
    +  str(urllib.parse.quote(route)))
    req = conn.getresponse()
    #req.add_header('User-Agent', User_Agent)
    
    if int(req.status) == 200 :
        print("\n 검색 완료!")
        return extractRoute(req.read().decode("utf-8"))
    conn.close()
    pass

def extractRoute(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    listElements = tree.getiterator("list")
    for list in listElements:
        direction = list.find("direction")
        routeName = list.find("routeName")
        serviceAreaName = list.find("serviceAreaName")

        print('===========================')
        print("노선명:", routeName.text)
        print("방향:", direction.text)
        print("경로 이름:", serviceAreaName.text)
        print('============================')
#        if len(menu.text) > 0 :
#            return {"routeName":routeName.text, "menu":menu.text}
    pass
#==============================================================================

def printmenu():
    print("\n 엄마 휴게소 얼마나 걸려? ") 
    print("==========Menu========")
    print("   휴게소로 검색 : 1")
    print("   경로로 검색 : 2")
    print("   프로그램 종료 : ㅂ")
    print("=====================")

def launcherFunction(menu):
    global loopflag    
    
    if menu == '1':
        serviceArea = str(input ('Service Area Name: '))
        getDataFromServiceArea(serviceArea)
    elif menu == '2':
        routeName = str(input('Route Name: '))
        getDataFromServiceArea(routeName)
    elif menu =='ㅂ':
        loopflag = 0

##### run #####
while(loopflag > 0):
    printmenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("엄마! 알겠어! 그거 먹자!")
