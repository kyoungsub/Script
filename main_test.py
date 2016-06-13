# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        self.map_tab = QtWidgets.QWidget()
        self.map_tab.setObjectName("map_tab")
        self.webView = QtWebKitWidgets.QWebView(self.map_tab)
        self.webView.setGeometry(QtCore.QRect(20, 20, 481, 341))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.Top.addTab(self.map_tab, "")

        self.retranslateUi(Dialog)
        self.Top.setCurrentIndex(2)
        self.Search.setCurrentIndex(1)
        self.search_button_route.clicked.connect(Dialog.searching_route)
        self.search_button_area.clicked.connect(Dialog.searching_area)
        self.search_list_area.clicked['QModelIndex'].connect(self.result_area.update)
        self.search_list_route.clicked['QModelIndex'].connect(self.result_route.update)
        self.search_list_route.clicked['QModelIndex'].connect(Dialog.set_route)
        self.search_list_area.clicked['QModelIndex'].connect(Dialog.set_area)
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
        self.Top.setTabText(self.Top.indexOf(self.map_tab), _translate("Dialog", "지도로 보기"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

