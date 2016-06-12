# -*- coding: utf-8 -*-

#import urllib

import http.client
import urllib

# C/C++ 모듈 연동
import price

#GUI를 위한 PyQT 기본 모듈
from PyQt5 import QtCore, QtGui, QtWidgets

from xml.etree import ElementTree
#global
loopflag = 1

class Ui_Dialog(object):
    def __init__(self):
        self.directionList_area =[]
        self.serviceAreaNameList_area =[]
        self.menuList_area =[]
        self.salePriceList_area =[]

        self.directionList_route =[]
        self.serviceAreaNameList_route =[]
        self.menuList_route =[]
        self.salePriceList_route =[]
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 411)
        Dialog.setMinimumSize(QtCore.QSize(537, 411))
        Dialog.setMaximumSize(QtCore.QSize(537, 411))
        self.Top = QtWidgets.QTabWidget(Dialog)
        self.Top.setGeometry(QtCore.QRect(0, 0, 531, 411))
        self.Top.setMinimumSize(QtCore.QSize(531, 411))
        self.Top.setMaximumSize(QtCore.QSize(531, 411))
        self.Top.setObjectName("Top")
        self.search_tab = QtWidgets.QWidget()
        self.search_tab.setObjectName("search_tab")
        self.Search = QtWidgets.QTabWidget(self.search_tab)
        self.Search.setGeometry(QtCore.QRect(0, 0, 531, 391))
        self.Search.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Search.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Search.setObjectName("Search")
        self.ServiceArea = QtWidgets.QWidget()
        self.ServiceArea.setObjectName("ServiceArea")
        self.result_area = QtWidgets.QTreeWidget(self.ServiceArea)
        self.result_area.setGeometry(QtCore.QRect(190, 20, 311, 221))
        self.result_area.setMaximumSize(QtCore.QSize(311, 16777215))
        self.result_area.setObjectName("result_area")
        item_0 = QtWidgets.QTreeWidgetItem(self.result_area)
        self.search_list_area = QtWidgets.QListWidget(self.ServiceArea)
        self.search_list_area.setGeometry(QtCore.QRect(20, 20, 141, 321))
        self.search_list_area.setObjectName("search_list_area")
        self.layoutWidget = QtWidgets.QWidget(self.ServiceArea)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 260, 311, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.search_bar_area = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.search_bar_area.setContentsMargins(0, 0, 0, 0)
        self.search_bar_area.setObjectName("search_bar_area")
        self.search_text_area = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_text_area.setObjectName("search_text_area")
        self.search_bar_area.addWidget(self.search_text_area)
        self.search_button_area = QtWidgets.QPushButton(self.layoutWidget)
        self.search_button_area.setObjectName("search_button_area")
        self.search_bar_area.addWidget(self.search_button_area)
        self.Search.addTab(self.ServiceArea, "")
        self.RouteName = QtWidgets.QWidget()
        self.RouteName.setObjectName("RouteName")
        self.search_list_route = QtWidgets.QListWidget(self.RouteName)
        self.search_list_route.setGeometry(QtCore.QRect(20, 20, 141, 321))
        self.search_list_route.setObjectName("search_list_route")
        self.result_route = QtWidgets.QTreeWidget(self.RouteName)
        self.result_route.setGeometry(QtCore.QRect(190, 20, 311, 221))
        self.result_route.setObjectName("result_route")
        item_0 = QtWidgets.QTreeWidgetItem(self.result_route)
        self.layoutWidget1 = QtWidgets.QWidget(self.RouteName)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 260, 311, 73))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.search_bar_route = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.search_bar_route.setContentsMargins(0, 0, 0, 0)
        self.search_bar_route.setObjectName("search_bar_route")
        self.search_text_route = QtWidgets.QLineEdit(self.layoutWidget1)
        self.search_text_route.setObjectName("search_text_route")
        self.search_bar_route.addWidget(self.search_text_route)
        self.search_button_route = QtWidgets.QPushButton(self.layoutWidget1)
        self.search_button_route.setObjectName("search_button_route")
        self.search_bar_route.addWidget(self.search_button_route)
        self.Search.addTab(self.RouteName, "")
        self.Top.addTab(self.search_tab, "")
        self.chart_tab = QtWidgets.QWidget()
        self.chart_tab.setObjectName("chart_tab")
        self.Top.addTab(self.chart_tab, "")

        self.retranslateUi(Dialog)
        self.Top.setCurrentIndex(0)
        self.Search.setCurrentIndex(0)
        self.search_button_route.clicked.connect(self.searching_route)
        self.search_button_area.clicked.connect(self.searching_area)
        self.search_list_area.clicked['QModelIndex'].connect(self.result_area.update)
        self.search_list_route.clicked['QModelIndex'].connect(self.result_route.update)
        self.search_list_route.clicked['QModelIndex'].connect(self.set_route)
        self.search_list_area.clicked['QModelIndex'].connect(self.set_area)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search_button_area, self.search_list_area)
        Dialog.setTabOrder(self.search_list_area, self.result_area)
        Dialog.setTabOrder(self.result_area, self.Search)
        Dialog.setTabOrder(self.Search, self.search_button_route)
        Dialog.setTabOrder(self.search_button_route, self.search_list_route)
        Dialog.setTabOrder(self.search_list_route, self.result_route)
        Dialog.setTabOrder(self.result_route, self.Top)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.result_area.headerItem().setText(0, _translate("Dialog", "휴게소명"))
        self.result_area.headerItem().setText(1, _translate("Dialog", "방향"))
        self.result_area.headerItem().setText(2, _translate("Dialog", "메뉴"))
        self.result_area.headerItem().setText(3, _translate("Dialog", "가격"))
        self.search_button_area.setText(_translate("Dialog", "검색"))
        self.Search.setTabText(self.Search.indexOf(self.ServiceArea), _translate("Dialog", "휴게소명으로 검색"))
        self.result_route.headerItem().setText(0, _translate("Dialog", "휴게소명"))
        self.result_route.headerItem().setText(1, _translate("Dialog", "방향"))
        self.result_route.headerItem().setText(2, _translate("Dialog", "메뉴"))
        self.result_route.headerItem().setText(3, _translate("Dialog", "가격"))
        self.search_button_route.setText(_translate("Dialog", "검색"))
        self.Search.setTabText(self.Search.indexOf(self.RouteName), _translate("Dialog", "경로명으로 검색"))
        self.Top.setTabText(self.Top.indexOf(self.search_tab), _translate("Dialog", "검색 기능"))
        self.Top.setTabText(self.Top.indexOf(self.chart_tab), _translate("Dialog", "차트로 보기"))

    def searching_route(self):
        routeName = str(self.search_text_route.text())
        self.getDataFromRouteName(routeName)

    def searching_area(self):
        serviceArea = str(self.search_text_area.text())
        self.getDataFromServiceArea(serviceArea)

    def set_route(self, QModelIndex):
        self.result_route.topLevelItem(0).setText(0, self.serviceAreaNameList_route[QModelIndex.row()])
        self.result_route.topLevelItem(0).setText(1, self.directionList_route[QModelIndex.row()])
        self.result_route.topLevelItem(0).setText(2, self.menuList_route[QModelIndex.row()])
        self.result_route.topLevelItem(0).setText(3, self.salePriceList_route[QModelIndex.row()])

    
    def set_area(self, QModelIndex):
        self.result_area.topLevelItem(0).setText(0, self.serviceAreaNameList_area[QModelIndex.row()])
        self.result_area.topLevelItem(0).setText(1, self.directionList_area[QModelIndex.row()])
        self.result_area.topLevelItem(0).setText(2, self.menuList_area[QModelIndex.row()])
        self.result_area.topLevelItem(0).setText(3, self.salePriceList_area[QModelIndex.row()])



    #========================== 휴게소명 검색 ======================================
    def getDataFromServiceArea(self, serviceArea):
        conn = http.client.HTTPConnection("data.ex.co.kr")
        conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&serviceAreaName="
        +  str(urllib.parse.quote(serviceArea)))
        req = conn.getresponse()
        #req.add_header('User-Agent', User_Agent)
        
        if int(req.status) == 200 :
            return self.extractArea(req.read().decode("utf-8"))
        conn.close()
        pass

    def extractArea(self, strXml):
        self.search_list_area.clear()

        self.directionList_area[:] = []
        self.serviceAreaNameList_area[:] =[]
        self.menuList_area[:] = []
        self.salePriceList_area[:] =[]
        
        tree = ElementTree.fromstring(strXml)
        listElements = tree.getiterator("list")
        
        dataElements = tree.getiterator("data")
        for i in dataElements:
            cnt = i.find("count")
            
        if cnt.text != '0':
            print("\n검색 완료!")
            for list in listElements:
                menu = list.find("batchMenu")
                if(menu != None):
                    self.menuList_area.append(menu.text)
                    salePrice = list.find("salePrice")
                    self.salePriceList_area.append(salePrice.text)
                    direction = list.find("direction")
                    self.directionList_area.append(direction.text)
                    serviceAreaName = list.find("serviceAreaName")
                    self.serviceAreaNameList_area.append(serviceAreaName.text)
                    print('===========================')
                    print("방향:", direction.text)
                    print("휴게소 이름:", serviceAreaName.text, "휴게소")
                    print("가격:", salePrice.text)
                    print("메뉴:", menu.text)
                    print('===========================')
                    self.search_list_area.addItem(serviceAreaName.text)

                    # C/C++ 연동 함수 호출 및 출력
                    print(price.check(menu.text))
        else:
            print('\n그런 곳 없음ㅋ')
            
    #        if len(menu.text) > 0 :
    #            return {"serviceAreaName":serviceAreaName.text, "menu":menu.text}
        pass
    #==============================================================================

    #============================ 경로 검색 ========================================
    def getDataFromRouteName(self, route):
        conn = http.client.HTTPConnection("data.ex.co.kr")
        conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=d%2Bgpbsvn3Vl5kqm1vaj9PqFxvOKhhGQ74xWyyrZG7803Gpkg%2BRsycotbu0JZ8sIVDT5jbpE2Ey5DzZdSXAVB2g%3D%3D&type=xml&routeName="
        +  str(urllib.parse.quote(route)))
        req = conn.getresponse()
        #req.add_header('User-Agent', User_Agent)
        
        if int(req.status) == 200 :
            return self.extractRoute(req.read().decode("utf-8"))
        conn.close()
        pass

    def extractRoute(self, strXml):
        self.search_list_route.clear()

        self.directionList_route[:] = []
        self.serviceAreaNameList_route[:] =[]
        self.menuList_route[:] = []
        self.salePriceList_route[:] =[]
        
        tree = ElementTree.fromstring(strXml)
        listElements = tree.getiterator("list")

        dataElements = tree.getiterator("data")
        for i in dataElements:
            cnt = i.find("count")    
        
        if cnt.text != '0':
            print("\n검색 완료!")
            for list in listElements:
                menu = list.find("batchMenu")
                if(menu != None):
                    self.menuList_route.append(menu.text)
                    direction = list.find("direction")
                    self.directionList_route.append(direction.text)
                    serviceAreaName = list.find("serviceAreaName")
                    self.serviceAreaNameList_route.append(serviceAreaName.text)
                    salePrice = list.find("salePrice")
                    self.salePriceList_route.append(salePrice.text)
                    routeName = list.find("routeName")

                    print('===========================')
                    print("노선명:", routeName.text)
                    print("방향:", direction.text)
                    print("경로 이름:", serviceAreaName.text, "휴게소")
                    print('============================')
                    self.search_list_route.addItem(serviceAreaName.text)
                
        else:
            print('\n그런 곳 없음ㅋ')
        pass
    #==============================================================================


#def printmenu():
#    print("\n엄마 휴게소 얼마나 걸려? ") 
#    print("==========Menu========")
#    print("   휴게소로 검색 : 1")
#    print("   경로로 검색 : 2")
#    print("   프로그램 종료 : ㅂ")
#    print("=====================")

#def launcherFunction(menu):
#    global loopflag      
#    if menu == '1':
#        serviceArea = str(input ('Service Area Name: '))
#        getDataFromServiceArea(serviceArea)
#    elif menu == '2':
#        routeName = str(input('Route Name: '))
#        getDataFromRouteName(routeName)
#    elif menu =='ㅂ':
#        loopflag = 0


##### run #####
import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())

#while(loopflag > 0):
#    printmenu()
#    menuKey = str(input ('select menu :'))
#    launcherFunction(menuKey)
#else:
#    print ("엄마! 알겠어! 그거 먹자!")
