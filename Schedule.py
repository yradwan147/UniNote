from PyQt5 import QtCore, QtGui, QtWidgets
from models import Course, Student
import datetime


class Schedule(object):

    def __init__(self, id):
        sunday = []
        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        self.id = id
        student = Student.query.filter(Student.university_id == id).first()
        try:
            schedule = eval(student.schedule)
            sunday.extend(schedule['Sunday'].split(','))
            monday.extend(schedule['Monday'].split(','))
            tuesday.extend(schedule['Tuesday'].split(','))
            wednesday.extend(schedule['Wednesday'].split(','))
            thursday.extend(schedule['Thursday'].split(','))
        except:
            pass

        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UniNote")
        MainWindow.resize(955, 698)
        MainWindow.setStyleSheet("background: #1F2833;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setStyleSheet("background-color: #45A29E;\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-style: outset;\n"
                                   "font-size:18px;\n"
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
        self.Button1.setObjectName("Button1")
        self.verticalLayout.addWidget(self.Button1)
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setStyleSheet("background-color: #45A29E;\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-style: outset;\n"
                                   "font-size:18px;\n"
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
        self.Button2.setObjectName("Button2")
        self.verticalLayout.addWidget(self.Button2)
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setStyleSheet("background-color: #45A29E;\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-style: outset;\n"
                                   "font-size:18px;\n"
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
        self.Button3.setObjectName("Button3")
        self.verticalLayout.addWidget(self.Button3)
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setStyleSheet("background-color: #45A29E;\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-style: outset;\n"
                                   "font-size:18px;\n"
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
        self.Button4.setObjectName("Button4")
        self.verticalLayout.addWidget(self.Button4)
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setStyleSheet("background-color: #45A29E;\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "border-style: outset;\n"
                                   "font-size:18px;\n"
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
        self.Button5.setObjectName("Button5")
        self.verticalLayout.addWidget(self.Button5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:  #C5C6C7;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setStyleSheet("color:  #C5C6C7;")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "SUN"))
        self.Button2.setText(_translate("MainWindow", "MON"))
        self.Button3.setText(_translate("MainWindow", "TUE"))
        self.Button4.setText(_translate("MainWindow", "WED"))
        self.Button5.setText(_translate("MainWindow", "THU"))
        self.label.setText(_translate("MainWindow", "Today You Have:"))

        self.Button1.clicked.connect(self.btn1_clk)
        self.Button2.clicked.connect(self.btn2_clk)
        self.Button3.clicked.connect(self.btn3_clk)
        self.Button4.clicked.connect(self.btn4_clk)
        self.Button5.clicked.connect(self.btn5_clk)

    def btn1_clk(self):

        self.listWidget.clear()
        for x in self.sunday:
            self.listWidget.addItem(str(x).strip())

    def btn2_clk(self):

        self.listWidget.clear()
        for x in self.monday:
            self.listWidget.addItem(str(x).strip())

    def btn3_clk(self):

        self.listWidget.clear()
        for x in self.tuesday:
            self.listWidget.addItem(str(x).strip())

    def btn4_clk(self):

        self.listWidget.clear()
        for x in self.wednesday:
            self.listWidget.addItem(str(x).strip())

    def btn5_clk(self):

        self.listWidget.clear()
        for x in self.thursday:
            self.listWidget.addItem(str(x).strip())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Schedule(202000293)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
