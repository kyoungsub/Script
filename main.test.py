# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.Top.addTab(self.map_tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.Top.setCurrentIndex(2)
        self.Search.setCurrentIndex(1)
        QtCore.QObject.connect(self.search_button_route, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.searching_route)
        QtCore.QObject.connect(self.search_button_area, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.searching_area)
        QtCore.QObject.connect(self.search_list_area, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.result_area.update)
        QtCore.QObject.connect(self.search_list_route, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.result_route.update)
        QtCore.QObject.connect(self.search_list_route, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), Dialog.set_route)
        QtCore.QObject.connect(self.search_list_area, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), Dialog.set_area)
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

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

