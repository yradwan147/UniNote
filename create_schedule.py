from PyQt5 import QtCore, QtGui, QtWidgets
from models import Student


class Schedule_Create(object):

    def __init__(self, id):
        self.id = id
        student = (Student.query.filter(
            Student.university_id == id).first())
        self.student = student

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 728)
        MainWindow.setStyleSheet("background: #1F2833;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 110, 891, 581))
        self.formLayoutWidget.setStyleSheet("")
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.l3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setStyleSheet("color :#C5C6C7;")
        self.l3.setObjectName("l3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l3)
        self.l4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setStyleSheet("color :#C5C6C7;")
        self.l4.setObjectName("l4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l4)
        self.l5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setStyleSheet("color :#C5C6C7;")
        self.l5.setObjectName("l5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.l5)
        self.l6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setStyleSheet("color :#C5C6C7;")
        self.l6.setObjectName("l6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.l6)
        self.l7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.l7.setFont(font)
        self.l7.setStyleSheet("color :#C5C6C7;")
        self.l7.setObjectName("l7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.l7)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setStyleSheet("border:3px solid #45A29E; color:white;")
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setStyleSheet("border:3px solid #45A29E; color:white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setStyleSheet("border:3px solid #45A29E; color:white;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_4.setStyleSheet("border:3px solid #45A29E; color:white;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_5.setStyleSheet("border:3px solid #45A29E; color:white;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.b1 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet("background-color: #45A29E;\n"
"\n"
"\n"
"\n"
"border-style: outset;\n"
"font-size:20px;\n"
"\n"
"\n"
"border-width: 2px;border-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-color: beige;\n"
"\n"
"\n"
"\n"
"font: bold 14px;\n"
"\n"
"\n"
"\n"
"min-width: 10em;\n"
"\n"
"\n"
"\n"
"padding: 6px;\n"
"\n"
"\n"
"\n"
"color:#c5c6c7")
        self.b1.setObjectName("b1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.b1)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(270, 20, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("color :#C5C6C7;")
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.b1.clicked.connect(self.pressed)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l3.setText(_translate("MainWindow", "Sunday"))
        self.l4.setText(_translate("MainWindow", "Monday"))
        self.l5.setText(_translate("MainWindow", "Tuesday"))
        self.l6.setText(_translate("MainWindow", "Wednesday"))
        self.l7.setText(_translate("MainWindow", "Thursday"))
        self.b1.setText(_translate("MainWindow", "Create"))
        self.l1.setText(_translate("MainWindow", "SCHEDULE"))

    # def setupUi(self, MainWindow):
    #     MainWindow.resize(1071, 935)
    #     self.centralwidget = QtWidgets.QWidget(MainWindow)

    #     self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
    #     self.formLayoutWidget.setGeometry(QtCore.QRect(170, 110, 761, 741))

    #     self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
    #     self.formLayout.setContentsMargins(0, 0, 0, 0)

    #     self.l3 = QtWidgets.QLabel(self.formLayoutWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l3.setFont(font)
    #     self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l3)

    #     self.l4 = QtWidgets.QLabel(self.formLayoutWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l4.setFont(font)
    #     self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.l4)

    #     self.t2 = QtWidgets.QTextEdit(self.formLayoutWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(
    #         QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(50)
    #     sizePolicy.setHeightForWidth(self.t2.sizePolicy().hasHeightForWidth())
    #     self.t2.setSizePolicy(sizePolicy)
    #     self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t2)

    #     self.t3 = QtWidgets.QTextEdit(self.formLayoutWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(
    #         QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(50)
    #     sizePolicy.setHeightForWidth(self.t3.sizePolicy().hasHeightForWidth())
    #     self.t3.setSizePolicy(sizePolicy)
    #     self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.t3)

    #     self.l5 = QtWidgets.QLabel(self.formLayoutWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l5.setFont(font)
    #     self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.l5)

    #     self.t4 = QtWidgets.QTextEdit(self.formLayoutWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(
    #         QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(50)
    #     sizePolicy.setHeightForWidth(self.t4.sizePolicy().hasHeightForWidth())
    #     self.t4.setSizePolicy(sizePolicy)
    #     self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.t4)

    #     self.l6 = QtWidgets.QLabel(self.formLayoutWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l6.setFont(font)
    #     self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.l6)

    #     self.t5 = QtWidgets.QTextEdit(self.formLayoutWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(
    #         QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(50)
    #     sizePolicy.setHeightForWidth(self.t5.sizePolicy().hasHeightForWidth())
    #     self.t5.setSizePolicy(sizePolicy)
    #     self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.t5)

    #     self.l7 = QtWidgets.QLabel(self.formLayoutWidget)
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l7.setFont(font)
    #     self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.l7)

    #     self.t6 = QtWidgets.QTextEdit(self.formLayoutWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(
    #         QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(50)
    #     sizePolicy.setHeightForWidth(self.t6.sizePolicy().hasHeightForWidth())
    #     self.t6.setSizePolicy(sizePolicy)
    #     self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.t6)

    #     self.l1 = QtWidgets.QLabel(self.centralwidget)
    #     self.l1.setGeometry(QtCore.QRect(440, 30, 150, 50))
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(22)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.l1.setFont(font)

    #     self.b1 = QtWidgets.QPushButton(self.centralwidget)
    #     self.b1.setGeometry(QtCore.QRect(510, 860, 91, 31))
    #     font = QtGui.QFont()
    #     font.setFamily("Times New Roman")
    #     font.setPointSize(18)
    #     font.setBold(True)
    #     font.setWeight(75)
    #     self.b1.setFont(font)
    #     MainWindow.setCentralWidget(self.centralwidget)

    #     self.menubar = QtWidgets.QMenuBar(MainWindow)
    #     self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
    #     MainWindow.setMenuBar(self.menubar)
    #     self.statusbar = QtWidgets.QStatusBar(MainWindow)
    #     MainWindow.setStatusBar(self.statusbar)
    #     self.retranslateUi(MainWindow)
    #     QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     self.l3.setText(_translate("MainWindow", "Sunday"))
    #     self.l4.setText(_translate("MainWindow", "Monday"))
    #     self.l5.setText(_translate("MainWindow", "Tuesday"))
    #     self.l6.setText(_translate("MainWindow", "Wednesday"))
    #     self.l7.setText(_translate("MainWindow", "Thursday"))
    #     self.l1.setText(_translate("MainWindow", "Schedule"))
    #     self.b1.setText(_translate("MainWindow", "Update"))

    def pressed(self):
        # Add placeholder text
        t_1 = self.textEdit.toPlainText()
        t_2 = self.textEdit_2.toPlainText()
        t_3 = self.textEdit_3.toPlainText()
        t_4 = self.textEdit_4.toPlainText()
        t_5 = self.textEdit_5.toPlainText()

        schedule = {'Sunday': t_1, 'Monday': t_2,
                    'Tuesday': t_3, 'Wednesday': t_4, 'Thursday': t_5}

        self.student.schedule = str(schedule)
        self.student.update()

        print(t_1, t_2, t_3, t_4, t_5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Schedule_Create(202000048)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
