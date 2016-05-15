# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtWidgets.QGroupBox(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 10, 301, 141))
        self.search.setObjectName("search")
        self.text_area = QtWidgets.QTextEdit(self.search)
        self.text_area.setGeometry(QtCore.QRect(10, 80, 131, 41))
        self.text_area.setObjectName("text_area")
        self.text_route = QtWidgets.QTextEdit(self.search)
        self.text_route.setGeometry(QtCore.QRect(10, 30, 131, 41))
        self.text_route.setObjectName("text_route")
        self.search_route = QtWidgets.QPushButton(self.search)
        self.search_route.setGeometry(QtCore.QRect(150, 30, 141, 41))
        self.search_route.setObjectName("search_route")
        self.search_area = QtWidgets.QPushButton(self.search)
        self.search_area.setGeometry(QtCore.QRect(150, 80, 141, 41))
        self.search_area.setObjectName("search_area")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(210, 170, 101, 51))
        self.Quit.setObjectName("Quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.search_route.clicked.connect(self.text_route.copy)
        self.search_area.clicked.connect(self.text_area.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setTitle(_translate("MainWindow", "검색"))
        self.text_route.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.search_route.setText(_translate("MainWindow", "노선명으로 검색"))
        self.search_area.setText(_translate("MainWindow", "휴게소명으로 검색"))
        self.Quit.setText(_translate("MainWindow", "종료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

