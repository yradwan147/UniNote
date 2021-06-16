

from PyQt5 import QtCore, QtGui, QtWidgets
from Resources_view import Ui_Dialog
from functools import partial
courses = ['PHYS002', 'CSCE002', 'MATH002']


class Ui_Courses(object):

    def __init__(self, courses):
        self.courses = courses

    def resources(self, course):
        print(course)
        self.r = QtWidgets.QDialog()
        self.ui = Ui_Dialog(course)
        self.ui.setupUi(self.r)
        self.r.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 555)
        MainWindow.setStyleSheet("background: #1F2833;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 501, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in self.courses:
            exec("self.pushButton" + i.strip() +
                 " = QtWidgets.QPushButton(self.verticalLayoutWidget)")
            eval("self.pushButton" + i.strip() + r".setStyleSheet('background-color: #45A29E;\nborder-style: outset;\nfont-size:18px;\nborder-width: 2px;border-radius: 10px;\nborder-color: beige;\nfont: bold 14px;\nmin-width: 10em;\npadding: 6px;\ncolor:#c5c6c7')")
            eval("self.pushButton" + i.strip() + ".setObjectName('pushButton" +
                 i.strip() + "')")
            eval("self.verticalLayout.addWidget(self.pushButton" +
                 i.strip() + ")")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color :#C5C6C7;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton.setText(_translate("MainWindow", "Course"))
        self.label.setText(_translate("MainWindow", "COURSES"))
        for i in self.courses:
            eval("self.pushButton"+i.strip() +
                 ".setText(_translate('MainWindow','"+i.strip()+"'))")
            eval("self.pushButton"+i.strip() +
                 ".clicked.connect(partial(self.resources, i.strip()))")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(courses)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
