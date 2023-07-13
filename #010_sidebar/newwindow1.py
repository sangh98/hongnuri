
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newwindow11(object):
    def setupUi(self, newwindow11):
        newwindow11.setObjectName("newwindow11")
        newwindow11.resize(943, 602)
        self.centralwidget = QtWidgets.QWidget(newwindow11)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("\n"
"background-color: rgb(42, 69, 98);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pagelabel1 = QtWidgets.QLabel(self.page)
        self.pagelabel1.setGeometry(QtCore.QRect(10, 10, 901, 511))
        self.pagelabel1.setStyleSheet("background-color: rgb(255, 255, 255);")

        #page1번 설명
        self.pagelabel1.setText("설명")
        self.pagelabel1.setObjectName("pagelabel1")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(730, 540, 181, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.page1undo = QtWidgets.QPushButton(self.widget)
        self.page1undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page1undo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/caret-back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page1undo.setIcon(icon)
        self.page1undo.setObjectName("page1undo")
        self.horizontalLayout_3.addWidget(self.page1undo)
        self.page1next = QtWidgets.QPushButton(self.widget)
        self.page1next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page1next.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/caret-forward.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page1next.setIcon(icon1)
        self.page1next.setObjectName("page1next")
        self.horizontalLayout_3.addWidget(self.page1next)
        self.stackedWidget.addWidget(self.page)

        # page 2번설명
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pagelabel2 = QtWidgets.QLabel(self.page_2)
        self.pagelabel2.setGeometry(QtCore.QRect(10, 10, 901, 511))
        self.pagelabel2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pagelabel2.setText("")
        self.pagelabel2.setObjectName("pagelabel2")
        self.page2next = QtWidgets.QPushButton(self.page_2)
        self.page2next.setGeometry(QtCore.QRect(823, 540, 86, 29))
        self.page2next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page2next.setText("")
        self.page2next.setIcon(icon1)
        self.page2next.setObjectName("page2next")
        self.page2undo = QtWidgets.QPushButton(self.page_2)
        self.page2undo.setGeometry(QtCore.QRect(730, 540, 86, 29))
        self.page2undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page2undo.setText("")
        self.page2undo.setIcon(icon)
        self.page2undo.setObjectName("page2undo")
        self.stackedWidget.addWidget(self.page_2)

        #page3번 설명
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pagelabel3 = QtWidgets.QLabel(self.page_3)
        self.pagelabel3.setGeometry(QtCore.QRect(11, 8, 899, 351))
        self.pagelabel3.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pagelabel3.setText("")
        self.pagelabel3.setObjectName("pagelabel3")
        self.page3undo = QtWidgets.QPushButton(self.page_3)
        self.page3undo.setGeometry(QtCore.QRect(720, 540, 93, 29))
        self.page3undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3undo.setText("")
        self.page3undo.setIcon(icon)
        self.page3undo.setObjectName("page3undo")
        self.page3next = QtWidgets.QPushButton(self.page_3)
        self.page3next.setGeometry(QtCore.QRect(820, 540, 93, 29))
        self.page3next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3next.setText("")
        self.page3next.setIcon(icon1)
        self.page3next.setObjectName("page3next")
        self.widget1 = QtWidgets.QWidget(self.page_3)
        self.widget1.setGeometry(QtCore.QRect(10, 364, 901, 171))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.page3quest1 = QtWidgets.QRadioButton(self.widget1)
        self.page3quest1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3quest1.setObjectName("page3quest1")
        self.verticalLayout_2.addWidget(self.page3quest1)
        self.page3quest2 = QtWidgets.QRadioButton(self.widget1)
        self.page3quest2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3quest2.setObjectName("page3quest2")
        self.verticalLayout_2.addWidget(self.page3quest2)
        self.page3quest3 = QtWidgets.QRadioButton(self.widget1)
        self.page3quest3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3quest3.setObjectName("page3quest3")
        self.verticalLayout_2.addWidget(self.page3quest3)
        self.page3quest4 = QtWidgets.QRadioButton(self.widget1)
        self.page3quest4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3quest4.setObjectName("page3quest4")
        self.verticalLayout_2.addWidget(self.page3quest4)
        self.page3quest5 = QtWidgets.QRadioButton(self.widget1)
        self.page3quest5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3quest5.setObjectName("page3quest5")
        self.verticalLayout_2.addWidget(self.page3quest5)
        self.stackedWidget.addWidget(self.page_3)

        # 페이지4번설명
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.layoutWidget = QtWidgets.QWidget(self.page_4)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 366, 901, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(720, 540, 195, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.page4undo = QtWidgets.QPushButton(self.layoutWidget_2)
        self.page4undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4undo.setText("")
        self.page4undo.setIcon(icon)
        self.page4undo.setObjectName("page4undo")
        self.horizontalLayout_4.addWidget(self.page4undo)
        self.page4next = QtWidgets.QPushButton(self.layoutWidget_2)
        self.page4next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4next.setText("")
        self.page4next.setIcon(icon1)
        self.page4next.setObjectName("page4next")
        self.horizontalLayout_4.addWidget(self.page4next)
        self.pagelabel4 = QtWidgets.QLabel(self.page_4)
        self.pagelabel4.setGeometry(QtCore.QRect(10, 7, 899, 351))
        self.pagelabel4.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pagelabel4.setText("")
        self.pagelabel4.setObjectName("pagelabel4")
        self.page4quest3 = QtWidgets.QRadioButton(self.page_4)
        self.page4quest3.setGeometry(QtCore.QRect(10, 434, 899, 19))
        self.page4quest3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4quest3.setObjectName("page4quest3")
        self.page4quest1 = QtWidgets.QRadioButton(self.page_4)
        self.page4quest1.setGeometry(QtCore.QRect(10, 370, 899, 19))
        self.page4quest1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4quest1.setObjectName("page4quest1")
        self.page4quest2 = QtWidgets.QRadioButton(self.page_4)
        self.page4quest2.setGeometry(QtCore.QRect(10, 402, 899, 19))
        self.page4quest2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4quest2.setObjectName("page4quest2")
        self.page4quest4 = QtWidgets.QRadioButton(self.page_4)
        self.page4quest4.setGeometry(QtCore.QRect(10, 466, 899, 19))
        self.page4quest4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4quest4.setObjectName("page4quest4")
        self.page4quest5 = QtWidgets.QRadioButton(self.page_4)
        self.page4quest5.setGeometry(QtCore.QRect(10, 498, 899, 19))
        self.page4quest5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4quest5.setObjectName("page4quest5")
        self.stackedWidget.addWidget(self.page_4)

        #page5번 설명
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.layoutWidget_3 = QtWidgets.QWidget(self.page_5)
        self.layoutWidget_3.setGeometry(QtCore.QRect(9, 366, 901, 161))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.page5quest1 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.page5quest1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5quest1.setObjectName("page5quest1")
        self.verticalLayout_5.addWidget(self.page5quest1)
        self.page5quest2 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.page5quest2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5quest2.setObjectName("page5quest2")
        self.verticalLayout_5.addWidget(self.page5quest2)
        self.page5quest3 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.page5quest3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5quest3.setObjectName("page5quest3")
        self.verticalLayout_5.addWidget(self.page5quest3)
        self.page5quest4 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.page5quest4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5quest4.setObjectName("page5quest4")
        self.verticalLayout_5.addWidget(self.page5quest4)
        self.page5quest5 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.page5quest5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5quest5.setObjectName("page5quest5")
        self.verticalLayout_5.addWidget(self.page5quest5)
        self.pagelabel5 = QtWidgets.QLabel(self.page_5)
        self.pagelabel5.setGeometry(QtCore.QRect(10, 10, 899, 351))
        self.pagelabel5.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pagelabel5.setText("")
        self.pagelabel5.setObjectName("pagelabel5")
        self.page5next = QtWidgets.QPushButton(self.page_5)
        self.page5next.setGeometry(QtCore.QRect(820, 540, 93, 29))
        self.page5next.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5next.setText("")
        self.page5next.setIcon(icon1)
        self.page5next.setObjectName("page5next")
        self.page5undo = QtWidgets.QPushButton(self.page_5)
        self.page5undo.setGeometry(QtCore.QRect(720, 540, 93, 29))
        self.page5undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page5undo.setText("")
        self.page5undo.setIcon(icon)
        self.page5undo.setObjectName("page5undo")
        self.stackedWidget.addWidget(self.page_5)

        #페이지 6설명
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.layoutWidget_5 = QtWidgets.QWidget(self.page_6)
        self.layoutWidget_5.setGeometry(QtCore.QRect(720, 540, 195, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.page6undo = QtWidgets.QPushButton(self.layoutWidget_5)
        self.page6undo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page6undo.setText("")
        self.page6undo.setIcon(icon)
        self.page6undo.setObjectName("page6undo")
        self.horizontalLayout_7.addWidget(self.page6undo)
        self.page6exit = QtWidgets.QPushButton(self.layoutWidget_5)
        self.page6exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page6exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page6exit.setIcon(icon2)
        self.page6exit.setObjectName("page6exit")
        self.horizontalLayout_7.addWidget(self.page6exit)
        self.pagelabel4_2 = QtWidgets.QLabel(self.page_6)
        self.pagelabel4_2.setGeometry(QtCore.QRect(10, 10, 901, 511))
        self.pagelabel4_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pagelabel4_2.setText("")
        self.pagelabel4_2.setObjectName("pagelabel4_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit.setGeometry(QtCore.QRect(90, 530, 51, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.page_6)
        self.label.setGeometry(QtCore.QRect(20, 530, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout.addWidget(self.stackedWidget)
        newwindow11.setCentralWidget(self.centralwidget)

        self.retranslateUi(newwindow11)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(newwindow11)

        #페이지 이동

        self.page1next.clicked.connect(self.go_to_next_page)
        self.page2next.clicked.connect(self.go_to_next_page)
        self.page3next.clicked.connect(self.go_to_next_page)
        self.page4next.clicked.connect(self.go_to_next_page)
        self.page5next.clicked.connect(self.go_to_next_page)
        
        self.page2undo.clicked.connect(self.go_to_previous_page)
        self.page3undo.clicked.connect(self.go_to_previous_page)
        self.page4undo.clicked.connect(self.go_to_previous_page)
        self.page5undo.clicked.connect(self.go_to_previous_page)
        self.page6undo.clicked.connect(self.go_to_previous_page)

    def go_to_next_page(self):
        # 다음 페이지로 이동하는 함수
        current_index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(current_index + 1)

    def go_to_previous_page(self):
        # 이전 페이지로 이동하는 함수
        current_index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(current_index - 1)

    def retranslateUi(self, newwindow11):
        _translate = QtCore.QCoreApplication.translate
        newwindow11.setWindowTitle(_translate("newwindow11", "MainWindow"))

        #페이지 3문제
        self.page3quest1.setText(_translate("newwindow11", "RadioButton"))
        self.page3quest2.setText(_translate("newwindow11", "RadioButton"))
        self.page3quest3.setText(_translate("newwindow11", "RadioButton"))
        self.page3quest4.setText(_translate("newwindow11", "RadioButton"))
        self.page3quest5.setText(_translate("newwindow11", "RadioButton"))

        #페이지 4문제
        self.page4quest3.setText(_translate("newwindow11", "RadioButton"))
        self.page4quest1.setText(_translate("newwindow11", "RadioButton"))
        self.page4quest2.setText(_translate("newwindow11", "RadioButton"))
        self.page4quest4.setText(_translate("newwindow11", "RadioButton"))
        self.page4quest5.setText(_translate("newwindow11", "RadioButton"))

        #페이지 5문제
        self.page5quest1.setText(_translate("newwindow11", "RadioButton"))
        self.page5quest2.setText(_translate("newwindow11", "RadioButton"))
        self.page5quest3.setText(_translate("newwindow11", "RadioButton"))
        self.page5quest4.setText(_translate("newwindow11", "RadioButton"))
        self.page5quest5.setText(_translate("newwindow11", "RadioButton"))
        self.label.setText(_translate("newwindow11", "점수"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newwindow11 = QtWidgets.QMainWindow()
    ui = Ui_newwindow11()
    ui.setupUi(newwindow11)
    newwindow11.show()
    sys.exit(app.exec_())
