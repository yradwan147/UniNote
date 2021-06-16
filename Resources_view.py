

from PyQt5 import QtCore, QtGui, QtWidgets
from models import Course
from functools import partial
import webbrowser


class Ui_Dialog(object):
    def __init__(self, courseName="PHYS002"):
        self.courseName = courseName

    def setupUi(self, Dialog):
        Dialog.setObjectName("UniNote")
        Dialog.resize(519, 622)
        Dialog.setStyleSheet("background:#1F2833;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font-size:38px;\n"
                                 "color:#c5c6c7")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        courseResourcesQuery = Course.query.filter(
            Course.name == self.courseName).first()
        resourcesList = eval((courseResourcesQuery.format())["resources"])
        for i in range(0, len(resourcesList)):
            exec("self.pushButton"+str(i)+" = QtWidgets.QPushButton(Dialog)")
            eval('self.pushButton'+str(i)).setStyleSheet("background-color: #45A29E;\n"
                                                         "border-style: outset;\n"
                                                         "font-size:20px;\n""border-width: 2px;border-radius: 10px;\n"
                                                         "border-color: beige;\n"
                                                         "font: bold 14px;\n"
                                                         "min-width: 10em;\n"
                                                         "padding: 6px;\n"
                                                         "color:#c5c6c7")

            exec('self.pushButton'+str(i) +
                 '.setObjectName("pushButton'+str(i)+'")')
            self.verticalLayout_2.addWidget(eval('self.pushButton' + str(i)))
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def goToLink(self, link):
        webbrowser.open(link)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.courseName))
        courseResourcesQuery = Course.query.filter(
            Course.name == self.courseName).first()
        resourcesList = eval((courseResourcesQuery.format())["resources"])

        for i in range(0, len(resourcesList)):
            eval('(self.pushButton' + str(i) +
                 ').setText(_translate("Dialog", "Resource name:" + str(resourcesList[0]["fileName"])))')
            eval("self.pushButton"+str(i).strip() +
                 ".clicked.connect(partial( self.goToLink, resourcesList[0]['fileLink']) ) ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
