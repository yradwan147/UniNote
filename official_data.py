from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from models import Official_Request, Student


class Data2(object):

    def __init__(self, id):
        self.id = id
        student = Student.query.filter(
            Student.university_id == id).first().format()
        if student['permissions'] != "Admin":
            self.flag = True

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(904, 814)       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #1F2833;")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.l1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.l1)
        self.l1.setStyleSheet("color :#C5C6C7;")

        self.tw = QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.tw.setFont(font)
        self.tw.setColumnCount(6)
        self.tw.setRowCount(0)
        self.tw.setStyleSheet("background: #C5C6C7;\n"
"border:2px solid rgb(69, 162, 158);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"\n"
"section{background-color:#45A29E};")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)        
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)        
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)       
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)        
        self.tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)       
        self.tw.setHorizontalHeaderItem(5, item)    
        self.verticalLayout.addWidget(self.tw)

        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.listit(MainWindow)

        self.load(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Requests Table"))
        self.l1.setText(_translate("MainWindow", "Requests"))

        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Student Email"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Request Title"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Request Body"))
        item = self.tw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))

    #Retrieving data from the database table "off_reqs" to view in the tablewidget
    
    def load(self, MainWindow):

        if self.flag:
            off_reqs = Official_Request.query.all()
        else:
            off_reqs = Official_Request.query.filter(
                Official_Request.stuID == self.id).all()
        req_list = [req.format() for req in off_reqs]

        i = 1
        tablerow = 0

        for req in req_list:
            self.tw.setRowCount(0+i)

            self.tw.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(req['stuName']))
            self.tw.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(req['stuID'])))
            self.tw.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(req['email']))
            self.tw.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(req['title']))
            self.tw.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(req['body']))
            self.tw.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(req['date']))

            tablerow += 1
            i += 1

    def exit(self):
        Data.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Data2(202000290)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
