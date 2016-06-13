# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import http.client
import urllib

# C/C++ 모듈 연동
import price

#GUI를 위한 PyQT 기본 모듈
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit

from xml.etree import ElementTree
#global
loopflag = 1

maphtml = '''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
.controls {
  margin-top: 10px;
  border: 1px solid transparent;
  border-radius: 2px 0 0 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  height: 32px;
  outline: none;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

#pac-input {
  background-color: #fff;
  font-family: Roboto;
  font-size: 15px;
  font-weight: 300;
  margin-left: 12px;
  padding: 0 11px 0 13px;
  text-overflow: ellipsis;
  width: 300px;
}

#pac-input:focus {
  border-color: #4d90fe;
}

.pac-container {
  font-family: Roboto;
}

#type-selector {
  color: #fff;
  background-color: #4d90fe;
  padding: 5px 11px 0px 11px;
}

#type-selector label {
  font-family: Roboto;
  font-size: 13px;
  font-weight: 300;
}

    </style>
    <title>Places Searchbox</title>
    <style>
      #target {
        width: 345px;
      }
    </style>
  </head>
  <body>
    <input id="pac-input" class="controls" type="text" placeholder="Search Box">
    <div id="map"></div>
    <script>

    function initAutocomplete() {
      var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 36.297598, lng: 127.598824},
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      });

      var input = document.getElementById('pac-input');
      var searchBox = new google.maps.places.SearchBox(input);
      map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

      map.addListener('bounds_changed', function() {
        searchBox.setBounds(map.getBounds());
      });

      var markers = [];
      searchBox.addListener('places_changed', function() {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
          return;
        }

        markers.forEach(function(marker) {
          marker.setMap(null);
        });
        markers = [];

        var bounds = new google.maps.LatLngBounds();
        places.forEach(function(place) {
          var icon = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
          };

          markers.push(new google.maps.Marker({
            map: map,
            icon: icon,
            title: place.name,
            position: place.geometry.location
          }));

          if (place.geometry.viewport) {
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        });
        map.fitBounds(bounds);
      });
    }


    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAL_Vct3v3gmxKl38DMrEGqdVCXtgOmtLk&libraries=places&callback=initAutocomplete"
         async defer></script>
  </body>
</html>
'''

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

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
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 411)
        Dialog.setMinimumSize(QtCore.QSize(537, 411))
        Dialog.setMaximumSize(QtCore.QSize(537, 411))
        self.Top = QtGui.QTabWidget(Dialog)
        self.Top.setGeometry(QtCore.QRect(0, 0, 531, 411))
        self.Top.setMinimumSize(QtCore.QSize(531, 411))
        self.Top.setMaximumSize(QtCore.QSize(531, 411))
        self.Top.setObjectName(_fromUtf8("Top"))
        self.search_tab = QtGui.QWidget()
        self.search_tab.setObjectName(_fromUtf8("search_tab"))
        self.Search = QtGui.QTabWidget(self.search_tab)
        self.Search.setGeometry(QtCore.QRect(0, 0, 531, 391))
        self.Search.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Search.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Search.setObjectName(_fromUtf8("Search"))
        self.ServiceArea = QtGui.QWidget()
        self.ServiceArea.setObjectName(_fromUtf8("ServiceArea"))
        self.result_area = QtGui.QTreeWidget(self.ServiceArea)
        self.result_area.setGeometry(QtCore.QRect(190, 20, 311, 221))
        self.result_area.setMaximumSize(QtCore.QSize(311, 16777215))
        self.result_area.setObjectName(_fromUtf8("result_area"))
        item_0 = QtGui.QTreeWidgetItem(self.result_area)
        self.search_list_area = QtGui.QListWidget(self.ServiceArea)
        self.search_list_area.setGeometry(QtCore.QRect(20, 20, 141, 321))
        self.search_list_area.setObjectName(_fromUtf8("search_list_area"))
        self.layoutWidget = QtGui.QWidget(self.ServiceArea)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 260, 311, 73))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.search_bar_area = QtGui.QHBoxLayout(self.layoutWidget)
        self.search_bar_area.setObjectName(_fromUtf8("search_bar_area"))
        self.search_text_area = QtGui.QLineEdit(self.layoutWidget)
        self.search_text_area.setObjectName(_fromUtf8("search_text_area"))
        self.search_bar_area.addWidget(self.search_text_area)
        self.search_button_area = QtGui.QPushButton(self.layoutWidget)
        self.search_button_area.setObjectName(_fromUtf8("search_button_area"))
        self.search_bar_area.addWidget(self.search_button_area)
        self.Search.addTab(self.ServiceArea, _fromUtf8(""))
        self.RouteName = QtGui.QWidget()
        self.RouteName.setObjectName(_fromUtf8("RouteName"))
        self.search_list_route = QtGui.QListWidget(self.RouteName)
        self.search_list_route.setGeometry(QtCore.QRect(20, 20, 141, 321))
        self.search_list_route.setObjectName(_fromUtf8("search_list_route"))
        self.result_route = QtGui.QTreeWidget(self.RouteName)
        self.result_route.setGeometry(QtCore.QRect(190, 20, 311, 221))
        self.result_route.setObjectName(_fromUtf8("result_route"))
        item_0 = QtGui.QTreeWidgetItem(self.result_route)
        self.layoutWidget1 = QtGui.QWidget(self.RouteName)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 260, 311, 73))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.search_bar_route = QtGui.QHBoxLayout(self.layoutWidget1)
        self.search_bar_route.setObjectName(_fromUtf8("search_bar_route"))
        self.search_text_route = QtGui.QLineEdit(self.layoutWidget1)
        self.search_text_route.setObjectName(_fromUtf8("search_text_route"))
        self.search_bar_route.addWidget(self.search_text_route)
        self.search_button_route = QtGui.QPushButton(self.layoutWidget1)
        self.search_button_route.setObjectName(_fromUtf8("search_button_route"))
        self.search_bar_route.addWidget(self.search_button_route)
        self.Search.addTab(self.RouteName, _fromUtf8(""))
        self.Top.addTab(self.search_tab, _fromUtf8(""))
        self.chart_tab = QtGui.QWidget()
        self.chart_tab.setObjectName(_fromUtf8("chart_tab"))
        self.Top.addTab(self.chart_tab, _fromUtf8(""))
        self.map_tab = QtGui.QWidget()
        self.map_tab.setObjectName(_fromUtf8("map_tab"))
        self.webView = QtWebKit.QWebView(self.map_tab)
        self.webView.setGeometry(QtCore.QRect(20, 20, 481, 341))
        #self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setHtml(maphtml)
        #self.webView.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.Top.addTab(self.map_tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.Top.setCurrentIndex(2)
        self.Search.setCurrentIndex(1)
        QtCore.QObject.connect(self.search_button_route, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searching_route)
        QtCore.QObject.connect(self.search_button_area, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searching_area)
        QtCore.QObject.connect(self.search_list_area, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.result_area.update)
        QtCore.QObject.connect(self.search_list_route, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.result_route.update)
        QtCore.QObject.connect(self.search_list_route, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.set_route)
        QtCore.QObject.connect(self.search_list_area, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.set_area)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search_button_area, self.search_list_area)
        Dialog.setTabOrder(self.search_list_area, self.result_area)
        Dialog.setTabOrder(self.result_area, self.Search)
        Dialog.setTabOrder(self.Search, self.search_button_route)
        Dialog.setTabOrder(self.search_button_route, self.search_list_route)
        Dialog.setTabOrder(self.search_list_route, self.result_route)
        Dialog.setTabOrder(self.result_route, self.Top)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.result_area.headerItem().setText(0, _translate("Dialog", "휴게소명", None))
        self.result_area.headerItem().setText(1, _translate("Dialog", "방향", None))
        self.result_area.headerItem().setText(2, _translate("Dialog", "메뉴", None))
        self.result_area.headerItem().setText(3, _translate("Dialog", "가격", None))
        self.search_button_area.setText(_translate("Dialog", "검색", None))
        self.Search.setTabText(self.Search.indexOf(self.ServiceArea), _translate("Dialog", "휴게소명으로 검색", None))
        self.result_route.headerItem().setText(0, _translate("Dialog", "휴게소명", None))
        self.result_route.headerItem().setText(1, _translate("Dialog", "방향", None))
        self.result_route.headerItem().setText(2, _translate("Dialog", "메뉴", None))
        self.result_route.headerItem().setText(3, _translate("Dialog", "가격", None))
        self.search_button_route.setText(_translate("Dialog", "검색", None))
        self.Search.setTabText(self.Search.indexOf(self.RouteName), _translate("Dialog", "경로명으로 검색", None))
        self.Top.setTabText(self.Top.indexOf(self.search_tab), _translate("Dialog", "검색 기능", None))
        self.Top.setTabText(self.Top.indexOf(self.chart_tab), _translate("Dialog", "차트로 보기", None))
        self.Top.setTabText(self.Top.indexOf(self.map_tab), _translate("Dialog", "지도로 보기", None))

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
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
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
